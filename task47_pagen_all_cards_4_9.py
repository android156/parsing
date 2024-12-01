import csv
from bs4 import BeautifulSoup
import requests

# Начальная страница
url = 'https://parsinger.ru/html/index1_page_1.html'
# Список куда будем складывать ссылки на карточки товаров со всех разделов всех страниц
hrefs = []
# Создаем сессию
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
                    page_urls = [a.get('href') for a in soup.select('a.name_item')]
                    hrefs.extend(page_urls)
                else:
                    print(f'Страница пагинации {url} не доступна. Код: {response.status_code}')
                print(f'Добавлено {len(page_urls)} ссылок со страницы №{i_page}')
        else:
            print(f'Страница секции {url} не доступна. Код: {response.status_code}')
    # Открываем файл для записи и записываем названия колонок
    with open('result.csv', 'w', encoding='utf-8-sig', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(
            ['Наименование', 'Артикул', 'Бренд', 'Модель',
             'Наличие', 'Цена', 'Старая цена', 'Ссылка'])
        # Проходим по всем карточкам товаров и собираем нужные данные
        for i, href_url in enumerate(hrefs, start=1):
            full_url = f'{schema}{href_url}'
            print(f'Обработка {i}/{len(hrefs)}: ', full_url)
            response = s.get(full_url)
            response.encoding = 'utf-8'
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'lxml')
                name = soup.select_one('p#p_header').text.strip()
                article = soup.select_one('p.article').text.split(': ')[1].strip()
                price = soup.select_one('span#price').text.strip()
                old_price = soup.select_one('span#old_price').text.strip()
                in_stock = soup.select_one('span#in_stock').text.split(': ')[1].strip()
                brand = soup.select_one('li#brand').text.split(': ')[1].strip()
                model = soup.select_one('li#model').text.split(': ')[1].strip()
                writer.writerow(
                    [name, article, brand, model, in_stock, price, old_price, full_url])
            else:
                print(f'Карточка товара {full_url} не доступна. Код: {response.status_code}')
