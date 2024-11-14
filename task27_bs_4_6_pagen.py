from bs4 import BeautifulSoup
import requests

#

url = 'http://parsinger.ru/html/index1_page_3.html'
response = requests.get(url=url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')
schema = 'http://parsinger.ru/html/'
# Ссылки к страницам, которые явно указаны в разделе пагинация
pagen = [f"{schema}{link['href']}" for link in soup.find('div', class_='pagen').find_all('a')]

print(pagen)

# Ищем номер последней страницы, если явно указан
url = 'http://parsinger.ru/html/index1_page_3.html'
response = requests.get(url=url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')
schema = 'http://parsinger.ru/html/'
pagen = [link.text for link in soup.find('div', class_='pagen').find_all('a')][-1]

print(pagen)

# Цикл по страницам пагинации, если не знаем и не нашли какая последняя
base_url = "https://ecofleks.ru/article.html?page="
num_page = 1  # начнем с первой страницы

# Создаем сессию
with requests.Session() as s:

    while True:
        url = f"{base_url}{num_page}"
        response = s.get(url)
        response.encoding = 'utf-8'
        # Если статус ответа 200, продолжаем парсинг
        if response.status_code == 200:
            # Здесь ваш код для парсинга содержимого страницы
            soup = BeautifulSoup(response.text, 'lxml')
            not_found = soup.select('div.not-found')
            if not_found:
                break
        else:
            # Если статус ответа не 200, завершаем цикл
            break
        num_page += 1
print(num_page - 1)
