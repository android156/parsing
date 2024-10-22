import random
import requests

# Указываем URL, к которому будем отправлять запрос для тестирования прокси
url = 'http://httpbin.org/ip'

# Открываем файл с прокси и читаем его
with open('proxy.txt') as file:

    # Считываем содержимое файла и разделяем его на строки
    proxy_file = file.read().split('\n')

    # Изменяем порядок следования прокси на случайный
    random.shuffle(proxy_file)

    # Перебираем прокси из списка
    for proxy_ in proxy_file:
        try:
            # Берем прокси из списка и удаляем лишние пробелы
            ip = proxy_.strip()
            print(proxy_)

            # Формируем словарь с прокси для http и https
            proxy = {
                'http': f'http://{ip}',
                'https': f'https://{ip}'
            }

            # Выполняем GET-запрос с использованием выбранного прокси
            response = requests.get(url=url, proxies=proxy)

            # Выводим результат в случае успешного подключения
            print(response.json(), 'Success connection')
        except Exception as _ex:

            # В случае неудачи пропускаем текущую итерацию
            continue