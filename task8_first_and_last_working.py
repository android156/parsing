import requests

first_available_page = 0
last_available_page = 0


# Создаем сессию
with requests.Session() as s:
    for i in range(1, 101):
        url = f'https://parsinger.ru/3.3/4/{i}.html'
        response = s.get(url)
        if response.status_code == 200:
            last_available_page = i
            if not first_available_page:
                first_available_page = i


print(f"Первая доступная страница: {first_available_page}.html")
print(f"Последняя доступная страница: {last_available_page}.html")