import requests

text = ''


# Создаем сессию
with requests.Session() as s:
    url = f'https://parsinger.ru/3.4/2/index.html'
    response = s.get(url)
    if response.status_code == 200:
        response.encoding = 'utf-8'
        text = response.text
        print(text)

