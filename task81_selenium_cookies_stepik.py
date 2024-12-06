import time

from selenium import webdriver
from datetime import datetime

# Пример куки с expiry в формате ISO 8601
cookies = [
    {
        'name': 'sessionid',
        'value': 'w08i4vurfnsculqpjbdwudl98pu5nwit',
        'domain': 'stepik.org',
        'path': '/',
        'expiry': '2024-09-08T09:22:31.119Z',
        'secure': True,
        'httpOnly': True
    },
    {
        'name': 'csrftoken',
        'value': 'QJ7KcveCtO8hze0qT7KSWFqTDSIlFZyMa3OrbqEtTsoN9TPnpemafpm6AA9BvhOj',
        'domain': 'stepik.org',
        'path': '/',
        'expiry': '2025-06-14T04:28:48.792Z',
        'secure': True,
        'httpOnly': False
    },
    {
        'name': 'tmr_detect',
        'value': '0%7C1733218804779',
        'domain': '.stepik.org',
        'path': '/',
        'expiry': '2025-01-25T03:33:13.326Z',
        'secure': False,
        'httpOnly': True
    }
]

# Преобразование строки даты ISO 8601 в Unix timestamp
for cookie in cookies:
    expiry_date = datetime.strptime(cookie['expiry'], "%Y-%m-%dT%H:%M:%S.%fZ")
    cookie['expiry'] = int(expiry_date.timestamp())

# Настройка WebDriver (в данном примере используется Chrome)
options = webdriver.ChromeOptions()
# options.add_argument("--headless")  # Запуск в фоновом режиме, если необходимо
driver = webdriver.Chrome(options=options)

# Перейдите на сайт Stepik для инициализации сессии
driver.get("https://stepik.org/")

# Добавьте куки в WebDriver
for cookie in cookies:
    driver.add_cookie(cookie)

# Перейдите на страницу, которая требует авторизации
driver.get("https://stepik.org/lesson/1108387/step/3")


# Проверка, что страница загружена правильно
print(driver.page_source)
time.sleep(10)
# Закрытие WebDriver
driver.quit()