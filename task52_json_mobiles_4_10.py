import csv
import json

from bs4 import BeautifulSoup
import requests

# Начальная страница
url = 'https://parsinger.ru/html/index2_page_1.html'
# Список куда будем складывать ссылки на карточки товаров со всех разделов всех страниц
hrefs = []
result_json = []

json_example = {
    "categories": "mobile",
    "name": "teXet TM-519R черный-красный Мобильный телефон",
    "article": "80397881",
    "description": {
        "brand": "Texet",
        "model": "TM-519R",
        "type": "Мобильный телефон",
        "material": "пластик",
        "type_display": "Цветной",
        "diagonal": "2.4",
        "size": "131,6x61,9x19 мм",
        "weight": "г 90.54",
        "resolution": "240x320",
        "site": "www.texet.ru"
    },
    "count": "31",
    "price": "2490 руб",
    "old_price": "2520 руб",
    "link": "https://parsinger.ru/html/mobile/2/2_1.html"
}

card_json = {
    "categories": "mobile",
}

# Создаем сессию
with requests.Session() as s:
    response = s.get(url)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')
    schema = 'https://parsinger.ru/html/'
    pagen = [f"{schema}{link['href']}" for link in soup.find('div', class_='pagen').find_all('a')]
    print(f'Раздел содержит {len(pagen)} страниц.')

    for i_page, page_url in enumerate(pagen, start=1):
        response = s.get(page_url)
        response.encoding = 'utf-8'
        # Если статус ответа 200, продолжаем парсинг
        if response.status_code == 200:
            # Собираем ссылки на карточки и добавляем в общий список ссылок на карточки
            soup = BeautifulSoup(response.text, 'lxml')
            page_urls = [a.get('href') for a in soup.select('a.name_item')]
            hrefs.extend(page_urls)
        else:
            print(f'Страница пагинации {url} не доступна. Код: {response.status_code}')
        print(f'Добавлено {len(page_urls)} ссылок со страницы №{i_page}')

    for i, href_url in enumerate(hrefs, start=1):
        full_url = f'{schema}{href_url}'
        print(f'Обработка {i}/{len(hrefs)}: ', full_url)
        response = s.get(full_url)
        response.encoding = 'utf-8'
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'lxml')
            li_list = soup.select('ul#description li')
            card_json = {
                "categories": "mobile",
                "name": soup.select_one('p#p_header').text.strip(),
                "article": soup.select_one('p.article').text.split(': ')[1].strip(),
                "description": dict(
                    zip([li.get('id') for li in li_list], [li.text.split(': ')[1].strip() for li in li_list])),
                "count": soup.select_one('span#in_stock').text.split(': ')[1].strip(),
                "price": soup.select_one('span#price').text.strip(),
                "old_price": soup.select_one('span#old_price').text.strip(),
                "link": full_url
            }
            result_json.append(card_json)


        else:
            print(f'Карточка товара {full_url} не доступна. Код: {response.status_code}')

    # Открываем файл для записи и записываем названия колонок
with open('result3.json', 'w', encoding='utf-8') as file:
    json.dump(result_json, file, indent=4, ensure_ascii=False)

from bs4 import BeautifulSoup
import requests
import json

result_list = list()

# # ща мы сделаем так, чтобы код не зависил от кол-ва электроники, хоть 32, хоть 132
# rq = requests.get(url='https://parsinger.ru/html/index2_page_1.html') # идем на 1 страницу товара
# syp = BeautifulSoup(rq.text, 'lxml') # суп
# last_link = syp.find('div', class_='pagen').find_all('a')[-1]['href'] # тут мы узнали последнюю страницу товара - index3_page_4.html
# rq = requests.get(url='https://parsinger.ru/html/' + last_link) # идем на эту страницу
# syp = BeautifulSoup(rq.text, 'lxml') # суп
# amount = int(syp.find_all('a', class_='name_item')[-1]['href'].rstrip('.html').split('_')[1])
# # помянем ваши глаза, но тут мы нашли число 32(кол-во товара) mouse/3/3_32.html => mouse/3/3_32 => ['mouse/3/3', '32'] => int(32)
#
# for page in range(1, amount + 1):
#     link = f'https://parsinger.ru/html/mobile/2/2_{page}.html' # формируем ссылку
#     req = requests.get(url=link)
#     req.encoding = 'utf-8'
#     soup = BeautifulSoup(req.text, 'lxml')
#     saver = dict() # тут собираем данные с каждой мышки
#     saver['categories'] = 'mobile' # категория
#     name = soup.find('p', id='p_header').text # имя
#     article = soup.find('p', class_='article').text.split(':')[1].strip() # артикул
#     description = {i['id']:i.text.split(':')[1].strip() for i in soup.find_all('li')} # собираем бренд и тд.
#     count = soup.find('span', id='in_stock').text.split(':')[1].strip() # кол-во
#     price = soup.find('span', id='price').text # цена
#     old_price = soup.find('span', id='old_price').text # старая цена
#     # теперь всё добавляем
#     saver['name'] = name
#     saver['article'] = article
#     saver['description'] = description
#     saver['count'] = count
#     saver['price'] = price
#     saver['old_price'] = old_price
#     saver['link'] = link
#     result_list.append(saver)
#
# with open('mouses.json', 'w', encoding='utf-8') as file:
#     json.dump(result_list, file, indent=4, ensure_ascii=False) # я еще на стадии изучения понял, что лучше сразу найти кол-во товара, а не писать 32, ведь надо быть готовым ко всему