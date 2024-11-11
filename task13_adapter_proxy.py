import requests
from requests.adapters import HTTPAdapter

# Список прокси
proxies_list = [
    {"http": "http://10.10.1.11:3128", "https": "socks5://10.10.10.11:3128"},
    {"http": "socks5://10.10.10.159:8000", "https": "socks5://10.10.10.159:8000"},
        #...
    {"http": "socks5://10.10.10.216:8000", "https": "socks5://10.10.10.216:8000"},
]
# Создание сессии
session = requests.Session()

def make_request(proxy):
    adapter = HTTPAdapter()
    session.mount('http://', adapter)
    session.mount('https://', adapter)

    try:
        response = session.get('https://httpbin.org/get', proxies=proxy, timeout=5)
        print(f'Успех с прокси {proxy}: {response.status_code}')
    except requests.exceptions.RequestException as e:
        print(f'Не удалось использовать прокси {proxy}: {str(e)}')
        return False   # Возврат False при неудачной попытке
    return True        # Возврат True при успешной попытке

# Перебор прокси и запросов
proxy_index = 0
for i in range(5):
    success = make_request(proxies_list[proxy_index])
    if not success:
        proxy_index = (proxy_index + 1) % len(proxies_list)       # Переход к следующему прокси
        success = make_request(proxies_list[proxy_index])         # Повторный запрос с новым прокси

# Закрытие сессии
session.close()