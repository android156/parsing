import json
from bs4 import BeautifulSoup
import requests

# Начальная страница
url = 'https://parsinger.ru/html/index1_page_1.html'

# Список куда будем складывать ссылки на карточки товаров со всех разделов всех страниц
hrefs = []
# словарь для импорта в JSON
result_json = []

# Создаем сессию
with requests.Session() as s:
    response = s.get(url)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')
    schema = 'https://parsinger.ru/html/'
    # Ссылки к разделам, которые явно указаны слева
    nav_menu = [f"{schema}{link['href']}" for link in soup.find('div', class_='nav_menu').find_all('a')]
    # Парсим названия категорий
    categories = {a.get('id'): a.get_text().strip() for a in soup.select('div.nav_menu > a div')}
    cat_for_url = []  # Список категорий соответствующий списку url карточек
    print(f'Обнаружено {len(nav_menu)} разделов: {list(categories.values())}.')

    for i_section, section_url in enumerate(nav_menu, start=1):
        print(f'Обработка раздела №{i_section} {list(categories.values())[i_section - 1]}: {section_url}')
        response = s.get(section_url)
        response.encoding = 'utf-8'
        # Если статус ответа 200, продолжаем парсинг
        soup = BeautifulSoup(response.text, 'lxml')
        pagen = [f"{schema}{link['href']}" for link in soup.find('div', class_='pagen').find_all('a')]
        print(f'Раздел содержит {len(pagen)} страниц.')
        if response.status_code == 200:
            for i_page, page_url in enumerate(pagen, start=1):
                cat_for_url.append(list(categories)[i_section - 1])
                response = s.get(page_url)
                response.encoding = 'utf-8'
                # Если статус ответа 200, продолжаем парсинг
                if response.status_code == 200:
                    # Собираем ссылки на карточки и добавляем в общий список ссылок на карточки
                    soup = BeautifulSoup(response.text, 'lxml')
                    page_urls = [a.get('href') for a in soup.select('a.name_item')]
                    hrefs.extend(page_urls)
                    cat_for_url.extend([list(categories)[i_section - 1]]*len(page_urls))
                else:
                    print(f'Страница пагинации {url} не доступна. Код: {response.status_code}')
                print(f'Добавлено {len(page_urls)} ссылок со страницы №{i_page}')
        else:
            print(f'Страница секции {url} не доступна. Код: {response.status_code}')

    # Проходим по всем карточкам товаров и собираем нужные данные
    for i, href_url in enumerate(hrefs, start=1):
        full_url = f'{schema}{href_url}'
        print(f'Обработка {i}/{len(hrefs)}: ', full_url)
        response = s.get(full_url)
        response.encoding = 'utf-8'
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'lxml')
            li_list = soup.select('ul#description li')
            # формируем словарь из карточки товара
            card_json = {
                "categories": cat_for_url[i - 1],
                "name": soup.select_one('p#p_header').text.strip(),
                "article": soup.select_one('p.article').text.split(': ')[1].strip(),
                "description": dict(
                    zip([li.get('id') for li in li_list], [li.text.split(': ')[1].strip() for li in li_list])),
                "count": soup.select_one('span#in_stock').text.split(': ')[1].strip(),
                "price": soup.select_one('span#price').text.strip(),
                "old_price": soup.select_one('span#old_price').text.strip(),
                "link": full_url
            }
            # Добавляем словарь этой карточки в словарь для импорта в JSON
            result_json.append(card_json)
        else:
            print(f'Карточка товара {full_url} не доступна. Код: {response.status_code}')
    print('Обработка всех карточек завершена.')
# Открываем файл для записи и записываем туда json
with open('result_160.json', 'w', encoding='utf-8') as file:
    json.dump(result_json, file, indent=4, ensure_ascii=False)
print('JSON сформирован.')

