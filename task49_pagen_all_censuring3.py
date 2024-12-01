
import csv
import requests
from bs4 import BeautifulSoup

# создание объекта сессии
session = requests.Session()

# создание файла csv

with open('res4.csv', 'w', encoding='utf-8-sig', newline='') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow([
        'Наименование', 'Артикул', 'Бренд', 'Модель', 'Наличие', 'Цена', 'Старая цена', 'Ссылка'])

# создание словаря меток для удобного перебора ссылок в цикле
labels = {1 :'watch',
          2 :'mobile',
          3 :'mouse',
          4 :'hdd',
          5 :'headphones'}

schema_base = 'https://parsinger.ru/html/'


for i in range(1 ,6):
    schema = schema_base + f'{labels[i]}/{i}/'
    for j in range(1 ,33):
        url = schema + f'{i}_{j}.html'
        response = session.get(url=url)
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, 'lxml')

        # Извлекаем имена и другие характеристики  товаров и убираем лишние пробелы
        name = [x.text.strip() for x in soup.find_all('p', id='p_header')]
        article = [(((x.text.strip()).split(':'))[1]).strip() for x in soup.find_all('p', class_='article')]
        brand = [(((x.text.strip()).split(':'))[1]).strip() for x in soup.find_all('li', id='brand')]
        model = [(((x.text.strip()).split(':'))[1]).strip() for x in soup.find_all('li', id='model')]
        stock = [(((x.text.strip()).split(':'))[1]).strip() for x in soup.find_all('span', id='in_stock')]

        # Извлекаем цены товаров
        price = [x.text for x in soup.find_all('span', id='price')]
        old_price = [x.text for x in soup.find_all('span', id='old_price')]

        # Запишем ссылку в список, чтобы она правильно записалась в таблице через zip (а не только буква "h")
        link = []
        link.append(url)


        # Открываем файл для дополнительной записи данных
        with open('res4.csv', 'a', encoding='utf-8-sig', newline='') as file:
            writer = csv.writer(file, delimiter=';')
            for name, article, brand, model, stock, price, old_price, link in zip(name, article, brand, model, stock, price, old_price, link):

                # Формируем строку для записи
                flatten = name, article, brand, model, stock, price, old_price, link
                writer.writerow(flatten)

print('Файл res4.csv создан')
