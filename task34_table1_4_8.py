import requests
from bs4 import BeautifulSoup


url = 'https://parsinger.ru/table/1/index.html'
response = requests.get(url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'html.parser')

# Ищем первую таблицу на странице
table = soup.find('table')

# Извлекаем заголовки таблицы, пройдясь по всем элементам th в таблице и получив их текст
headers = [header.text for header in table.find_all('th')]

# Извлекаем строки таблицы, начиная со второй (индекс 1), так как первая строка - это заголовки
rows = table.find_all('tr')[1:]

# Создаём пустой список для данных
data_set = set()

# Проходим по каждой строке в таблице
for row in rows:
    [data_set.add(float(cell.text)) for cell in row.find_all('td')]

print(sum(data_set))


# table = soup.find_all('td')
# print(sum(set([float(num.text) for num in table])))