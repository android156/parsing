import requests

resp_sum = 0


# Создаем сессию
with requests.Session() as s:
    for i in range(1, 201):
        url = f'https://parsinger.ru/3.3/2/{i}.html'
        response = s.get(url)
        resp_sum += response.status_code

print(resp_sum)
