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
                # Здесь ваш код для парсинга содержимого страницы
                soup = BeautifulSoup(response.text, 'lxml')
                items_blocks = soup.select('div.img_box')
                for item in items_blocks:
                    it_link = item.select_one('div.sale_button a').get('href')
                    link_list.append(it_link)
            else:
                # Если статус ответа не 200, завершаем цикл
                break
            num_page += 1
res = 0
with requests.Session() as s:
    for link in link_list:
        response = s.get(base_url + link)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'lxml')
            in_stock = get_num_value(soup.select_one('span#in_stock').get_text())
            price = get_num_value(soup.select_one('span#price').get_text())
            res += in_stock * price
print(res, len(link_list))

# Сохраняем результат в буфер обмена
# pyperclip.copy(mouse_lists)
