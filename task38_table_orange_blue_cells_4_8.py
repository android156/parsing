import requests
from bs4 import BeautifulSoup


url = 'https://parsinger.ru/table/5/index.html'
response = requests.get(url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'html.parser')

# Ищем первую таблицу на странице
table = soup.find('table')

# Извлекаем заголовки таблицы, пройдясь по всем элементам th в таблице и получив их текст
headers = [header.text for header in table.find_all('th')]

# Извлекаем строки таблицы, начиная со второй (индекс 1), так как первая строка - это заголовки
rows = table.find_all('tr')[1:]


# Проходим по каждой строке в таблице

total = 0

for row in rows:
    orange = float(row.select_one('td.orange').text)
    blue = float(row.select_one('td:last-child').text)
    total += orange * blue

print(total)