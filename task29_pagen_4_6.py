import re

from bs4 import BeautifulSoup, Tag
import requests


def get_num_value(my_text):
    found_float = re.search(r'\d+(?:\.\d+)?', my_text)
    if found_float:
        return float(found_float.group())


num_page = 1  # начнем с первой страницы
base_url = f"https://parsinger.ru/html/"
link_list = []
# Создаем сессию
with requests.Session() as s:
    while True:
        url = f"https://parsinger.ru/html/index3_page_{num_page}.html"
        response = s.get(url)
        response.encoding = 'utf-8'
        # Если статус ответа 200, продолжаем парсинг
        if response.status_code == 200:
            # Здесь ваш код для парсинга содержимого страницы
            soup = BeautifulSoup(response.text, 'lxml')
            items_blocks = soup.select('div.img_box')
            for item in items_blocks:
                it_link = item.select_one('div.sale_button a').get('href')
                it_type = item.select_one('div.description li').next_sibling.next_sibling.text.strip()
                if 'мышь' in it_type.lower():
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
            art = get_num_value(soup.select_one('p.article').get_text())
            res += int(art)
print(res, len(link_list))

# Сохраняем результат в буфер обмена
# pyperclip.copy(mouse_lists)
