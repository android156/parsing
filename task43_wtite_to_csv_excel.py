import csv
import requests
from bs4 import BeautifulSoup


lst = ['one', 'two', 'three']

with open('res.csv', 'w', newline='', encoding='utf-8-sig') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow(lst)


# *******************************************************************************************


# 1 ------------------------------------------------------
with open('res.csv', 'w', encoding='utf-8-sig', newline='') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow([
        'Наименование', 'Артикул', 'Бренд', 'Модель',
        'Тип', 'Игровая', 'Размер', 'Разрешение','Подсветка',
        'Сайт производителя', 'В наличии', 'Цена'])
# 1 ------------------------------------------------------

# 2 ------------------------------------------------------
url = 'http://parsinger.ru/html/mouse/3/3_11.html'

response = requests.get(url=url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')
# 2 ------------------------------------------------------

# 3 ------------------------------------------------------
name = soup.find('p', id='p_header').text
article = soup.find('p', class_='article').text.split(': ')[1]
brand = soup.find('li', id='brand').text.split(': ')[1]
model = soup.find('li', id='model').text.split(': ')[1]
type = soup.find('li', id='type').text.split(': ')[1]
purpose = soup.find('li', id='purpose').text.split(': ')[1]
light = soup.find('li', id='light').text.split(': ')[1]
size = soup.find('li', id='size').text.split(': ')[1]
dpi = soup.find('li', id='dpi').text.split(': ')[1]
site = soup.find('li', id='site').text.split(': ')[1]
in_stock = soup.find('span', id='in_stock').text.split(': ')[1]
price = soup.find('span', id='price').text.split(' ')[0]
# 3 ------------------------------------------------------

# 4 ------------------------------------------------------
with open('res.csv', 'a', encoding='utf-8-sig', newline='') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow([
        name, article, brand, model,
        type, purpose, light, size, dpi,
        site, in_stock, price])
# 4 ------------------------------------------------------


# *******************************************************************************************

# 1 ------------------------------------------------------
with open('res.csv', 'w', encoding='utf-8-sig', newline='') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow([
        'Наименование', 'Цена', 'Бренд', 'Тип', 'Подключение', 'Игровая'])
# 1 ------------------------------------------------------

# 2 ------------------------------------------------------
url = 'http://parsinger.ru/html/index3_page_2.html'

response = requests.get(url=url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')
# 2 ------------------------------------------------------

# 3 ------------------------------------------------------
# Извлекаем имена товаров и убираем лишние пробелы
name = [x.text.strip() for x in soup.find_all('a', class_='name_item')]

# Извлекаем описание товаров и разбиваем на строки
description = [x.text.split('\n') for x in soup.find_all('div', class_='description')]

# Извлекаем цены товаров
price = [x.text for x in soup.find_all('p', class_='price')]
# 3 ------------------------------------------------------


# 4------------------------------------------------------
# Открываем файл для дополнительной записи данных
with open('res.csv', 'a', encoding='utf-8-sig', newline='') as file:
    writer = csv.writer(file, delimiter=';')
    for item, price, descr in zip(name, price, description):

        # Формируем строку для записи
        flatten = item, price, *[x.split(':')[1].strip() for x in descr if x]
        writer.writerow(flatten)

print('Файл res.csv создан')