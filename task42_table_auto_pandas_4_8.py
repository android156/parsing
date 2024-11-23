import requests
from bs4 import BeautifulSoup
import pandas as pd
import pyperclip
import json

url = 'https://parsinger.ru/4.8/6/index.html'
response = requests.get(url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'html.parser')

# Ищем первую таблицу на странице
table = soup.find('table')

# Извлекаем заголовки таблицы, пройдясь по всем элементам th в таблице и получив их текст
headers = [header.text for header in table.find_all('th')]

# Извлекаем строки таблицы, начиная со второй (индекс 1), так как первая строка - это заголовки
rows = table.find_all('tr')[1:]

# clear_table = []
# for row in rows:
#     clear_table.append([float(cell.text) for cell in row.find_all('td')])
#
# df = pd.DataFrame(clear_table, columns=headers)
html = pd.read_html('https://parsinger.ru/4.8/6/index.html', encoding='utf-8')

df = html[0]

print(df.describe())

print(df.info())

df['Стоимость авто'] = df['Стоимость авто'].astype(int)
df['Год выпуска'] = df['Год выпуска'].astype(int)
df['Тип двигателя'] = df['Тип двигателя'].astype(str)
df['Марка Авто'] = df['Марка Авто'].astype(str)

filtered_autos = df[(df['Стоимость авто'] <= 4000000) & (df['Год выпуска'] >= 2005) & (
        df['Тип двигателя'] == 'Бензиновый')].sort_values('Стоимость авто')

filtered_autos = filtered_autos[['Марка Авто', 'Год выпуска', 'Тип двигателя', 'Стоимость авто', ]]


print(filtered_autos.head(2))

res_json = filtered_autos.to_json(orient="records", force_ascii=False)
sorted_json = json.dumps(json.loads(res_json), indent=4, ensure_ascii=False)
print(sorted_json)
#
pyperclip.copy(sorted_json)

# # Запрашиваем данные с сайта
# response = requests.get("https://parsinger.ru/4.8/6/index.html")
# response.raise_for_status()
# response.encoding='utf-8'
# # Разбираем содержимое с помощью Beautiful Soup
# soup = BeautifulSoup(response.text, 'html.parser')
#
# # Ищем таблицу с данными
# table = soup.find('table')
# rows = table.find_all('tr')[1:] if table else []
#
# # Собираем данные в список словарей
# cars = []
# for row in rows:
#     columns = row.find_all('td')
#     car = {
#         "Марка Авто": columns[0].text,
#         "Год выпуска": int(columns[1].text),
#         "Тип двигателя": columns[4].text,
#         "Стоимость авто": int(columns[7].text.replace(',', ''))
#     }
#     cars.append(car)
#
# # Фильтруем список по заданным условиям
# filtered_cars = [car for car in cars if car["Стоимость авто"] <= 4000000 and car["Год выпуска"] >= 2005 and car["Тип двигателя"] == "Бензиновый"]
#
# # Сортируем список по стоимости
# sorted_cars = sorted(filtered_cars, key=lambda x: x["Стоимость авто"])
#
# # Конвертируем в JSON и выводим результат
# print(json.dumps(sorted_cars, indent=4, ensure_ascii=False))