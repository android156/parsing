import requests

text = ''


# Создаем сессию
with requests.Session() as s:
    for i in range(1, 201):
        url = f'https://parsinger.ru/3.3/1/{i}.html'
        response = s.get(url)
        if response.status_code == 200:
            text = response.text
            print(url, text)
            break



