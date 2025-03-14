import itertools
import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from seleniumwire import webdriver as wire_webdriver

class ProxyRotator:
    def __init__(self, proxies):
        # создает итератор, который будет перебирать прокси-сервера в цикле
        self.proxies = itertools.cycle(proxies)
        # хранит текущий используемый прокси-сервер
        self.current_proxy = None
        # счетчик запросов, для определения когда нужно сменить прокси-сервер
        self.request_counter = 0

    def change_proxy(self):
        # меняет текущий используемый прокси-сервер на следующий в списке
        self.current_proxy = next(self.proxies)
        # сбрасывает счетчик запросов
        self.request_counter = 0
        return self.current_proxy

    def get_proxy(self):
        # проверяет нужно ли сменить пр
        # проверяет нужно ли сменить прокси-сервер
        # где 2, означает, что прокси будут изменены после каждого второго запроса
        if self.request_counter % 2 == 0:
            self.change_proxy()
        # увеличивает счетчик запросов
        self.request_counter += 1
        return self.current_proxy


# 5.101.91.200:8000:TdWubd:s914RN
# 5.8.60.177:8000:TdWubd:s914RN
proxies = [
    {'http': "socks5://TdWubd:s914RN@5.101.91.200:8000", 'https': "socks5://TdWubd:s914RN@5.101.91.200:8000"},
    {'http': "socks5://TdWubd:s914RN@5.8.60.177:8000", 'https': "socks5://TdWubd:s914RN@5.8.60.177:8000"},
    # {'http': "socks5://4bL6Jn:SEKwVS@196.18.167.105:8000", 'https': "socks5://4bL6Jn:SEKwVS@196.18.167.105:8000"},
    # {'http': "socks5://wRKZPG:snFyfD@91.229.113.96:8000", 'https': "socks5://wRKZPG:snFyfD@91.229.113.96:8000"}
]

proxy_rotator = ProxyRotator(proxies)

while True:
    proxy = proxy_rotator.get_proxy()
    print(f'using proxy: {proxy}')
    prx = {}
    prx.update({'proxy': proxy})
    with wire_webdriver.Chrome(seleniumwire_options=prx) as browser:
        browser.get("http://httpbin.org/ip")
        print(browser.find_element(By.TAG_NAME, 'body').text)
        # тут любой код для работы на странице
        # тут любой код для работы на странице
        # тут любой код для работы на странице
        # тут любой код для работы на странице
        # тут любой код для работы на странице
        time.sleep(2)