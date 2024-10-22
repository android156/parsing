# Импортируем необходимые библиотеки
from fake_useragent import UserAgent
import requests
import time
from random import randint


# Функция для выполнения GET-запроса с подменой User-Agent
def make_request(url, headers):
    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code == 200:
            return response.text
        else:
            return f"Ошибка: получен статус-код {response.status_code}"
    except Exception as e:
        return f"Произошла ошибка: {e}"


# Инициализация
url = "http://httpbin.org/user-agent"
ua = UserAgent()

# Цикл для выполнения 10 запросов с разными User-Agent и случайными задержками
for i in range(10):
    fake_ua = {'User-Agent': ua.random}  # Генерация случайного User-Agent
    print(f"Итерация {i + 1} с User-Agent: {fake_ua['User-Agent']}")

    # Выполнение запроса
    response_text = make_request(url, fake_ua)
    print(f"Ответ сервера: {response_text}")

    # Случайная задержка от 1 до 5 секунд
    sleep_time = randint(1, 5)
    print(f"Задержка на {sleep_time} секунд")
    time.sleep(sleep_time)