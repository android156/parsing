import json
import time

from bs4 import BeautifulSoup
import requests

# Начальная страница
url = 'https://parsinger.ru/html/index1_page_1.html'
# Список куда будем складывать ссылки на карточки товаров со всех разделов всех страниц

headers = ['Наименование', 'Бренд', 'Тип подключения', 'Цвет', 'Тип наушников', 'Цена']
result_json = []

json_example = {
    "Наименование": "Crown CMGH-3100",
    "Бренд": "Crown",
    "Тип подключения": "Проводной",
    "Цвет": "черный, красный",
    "Тип наушников": "Мониторные",
    "Цена": "3110 руб"
}

def main():
    with requests.Session() as s:
        response = s.get(url)
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, 'lxml')
        schema = 'http://parsinger.ru/html/'
        # Ссылки к разделам, которые явно указаны слева
        nav_menu = [f"{schema}{link['href']}" for link in soup.find('div', class_='nav_menu').find_all('a')]
        print(f'Обнаружено {len(nav_menu)} разделов.')

        for i_section, section_url in enumerate(nav_menu, start=1):
            print(f'Обработка раздела {i_section}: {section_url}')
            response = s.get(section_url)
            response.encoding = 'utf-8'
            # Если статус ответа 200, продолжаем парсинг
            soup = BeautifulSoup(response.text, 'lxml')
            pagen = [f"{schema}{link['href']}" for link in soup.find('div', class_='pagen').find_all('a')]
            print(f'Раздел содержит {len(pagen)} страниц.')
            if response.status_code == 200:
                for i_page, page_url in enumerate(pagen, start=1):
                    response = s.get(page_url)
                    response.encoding = 'utf-8'
                    # Если статус ответа 200, продолжаем парсинг
                    if response.status_code == 200:
                        # Собираем ссылки на карточки и добавляем в общий список ссылок на карточки
                        soup = BeautifulSoup(response.text, 'lxml')
                        cards = soup.select('div.img_box')
                        for i_card, card in enumerate(cards, start=1):
                            print(f'Обработка {i_card}/{len(cards)}')
                            card_json = {'Наименование': card.select_one('a.name_item').text.strip()}
                            desc_els = dict([(el.split(': ')[0], el.split(': ')[1].strip()) for el in
                                             [desc_el.text.strip() for desc_el in card.select('div.description li')]])
                            card_json.update(desc_els)
                            card_json['Цена'] = card.select_one('p.price').text.strip()
                            result_json.append(card_json)
                    else:
                        print(f'Страница пагинации {url} не доступна. Код: {response.status_code}')
                    print(f'Добавлено {len(cards)} объектов со страницы №{i_page}')
            else:
                print(f'Страница секции {url} не доступна. Код: {response.status_code}')

        # Открываем файл для записи JSON
        with open('result2.json', 'w', encoding='utf-8') as file:
            json.dump(result_json, file, indent=4, ensure_ascii=False)

start = time.time()
main()
print(f'время: {time.time() - start}')

# data = []
# for i in range(1, 6):
#     for j in range(1, 5):
#         response = requests.get(f'https://parsinger.ru/html/index{i}_page_{j}.html')
#         response.encoding = 'utf-8'
#         soup = BeautifulSoup(response.text, 'lxml')
#         names = [i.text.strip() for i in soup.select('.name_item')]
#         descriptions = [i.text.strip().split('\n') for i in soup.select('div.description')]
#         prices = [i.text for i in soup.select('p.price')]
#
#         for name, description, price in zip(names, descriptions, prices):
#             item = dict([['Наименование', name],
#                          *[map(str.strip, i.split(':')) for i in description],
#                          ['Цена', price]])
#             data.append(item)
#
# with open('res.json', 'w', encoding='utf-8') as file:
#     json.dump(data, file, indent=4, ensure_ascii=False)
