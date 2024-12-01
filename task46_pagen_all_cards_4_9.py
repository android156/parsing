import csv
import re
from bs4 import BeautifulSoup, Tag
import requests


def get_num_value(my_text):
    found_float = re.search(r'\d+(?:\.\d+)?', my_text)
    if found_float:
        return float(found_float.group())



base_url = f"https://parsinger.ru/html/"
link_list = []
# Создаем сессию
with requests.Session() as s:
    for i in range(1, 6):
        num_page = 1  # начнем с первой страницы
        while True:
            url = f"https://parsinger.ru/html/index{i}_page_{num_page}.html"
            response = s.get(url)
            response.encoding = 'utf-8'
            # Если статус ответа 200, продолжаем парсинг
            if response.status_code == 200:
                # код для парсинга содержимого страницы
                soup = BeautifulSoup(response.text, 'lxml')
                items_blocks = soup.select('div.img_box')
                with open('res3.csv', 'a', encoding='utf-8-sig', newline='') as file:
                    writer = csv.writer(file, delimiter=';')
                    for item in items_blocks:
                        name = item.select_one('a.name_item').text.strip()
                        price = item.select_one('p.price').text.strip()
                        li_list = item.select('div.description li')
                        brand, _type, _form, capacity = [li.text.split(': ')[1].strip() for li in li_list]
                        print(name, brand, _type, _form, capacity, price)
                        writer.writerow([name, brand, _type, _form, capacity, price])
            else:
                # Если статус ответа не 200, завершаем цикл
                break
            num_page += 1


# Сохраняем результат в буфер обмена
# pyperclip.copy(mouse_lists)
