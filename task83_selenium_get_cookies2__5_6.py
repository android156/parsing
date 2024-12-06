import time
from pprint import pprint
from selenium import webdriver

with webdriver.Chrome() as webdriver:
    webdriver.get('https://parsinger.ru/methods/3/index.html')
    cookie_dict = webdriver.get_cookies()
    secret_cookies_values = [int(cookie['value']) for cookie in cookie_dict if
                             (int(cookie.get('name').split('_')[-1]) % 2 == 0 and cookie.get('name').startswith(
                                 'secret_cookie'))]
    pprint(cookie_dict)
    pprint(secret_cookies_values)
    print(sum(secret_cookies_values))
