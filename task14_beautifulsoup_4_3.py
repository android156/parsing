from bs4 import BeautifulSoup
import requests
import lxml

# Пример 3. Передача объекта response прямо из запроса
response = requests.get(url='http://parsinger.ru/html/watch/1/1_1.html')
response.encoding= 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')

# print(soup)

# from zipfile import ZipFile
# with ZipFile('index.zip', 'r') as archive:
#     file_to_read = archive.namelist()[0]

with open('index.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'lxml')

print(soup)


# Заметьте, что используется class_ вместо class, так как class является зарезервированным словом в Python.

# soup.find('tag', class_='your_class')

# Здесь 'data-attribute' - это имя пользовательского атрибута, а 'value' - его значение.

# soup.find('tag', {'data-attribute': 'value'})

