import requests
from bs4 import BeautifulSoup
import pandas as pd
import pyperclip # запись в буфер обмена.



url = 'https://parsinger.ru/4.8/7/index.html'
response = requests.get(url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'html.parser')

total_secret_number = 0
# Сохраняем все таблицы
tables = soup.find_all('table')
print(len(tables))
# Обрабатываем таблицы по очереди
for table in tables:
    rows = table.find_all('tr')
    total_secret_number += sum([int(cell.text) for row in rows for cell in row.find_all('td') if int(cell.text) % 3 == 0])


print(total_secret_number)

