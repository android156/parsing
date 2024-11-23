import requests
from bs4 import BeautifulSoup
import pandas as pd
import pyperclip



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

clear_table = []
for row in rows:
    clear_table.append([float(cell.text) for cell in row.find_all('td')])

df = pd.DataFrame(clear_table, columns=headers)


print(df)

print(df[headers[0]].sum().round(3))

col_dict = {}
for header in headers:
    # col_dict[header] = '{:.3f}'.format(df[header].sum().round(3))
    col_dict[header] = float(df[header].sum().round(3))

print(col_dict)

pyperclip.copy(col_dict)

# table = soup.find_all('td')
# print(sum(set([float(num.text) for num in table])))