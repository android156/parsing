import time
from pprint import pprint
from selenium import webdriver
from selenium.webdriver.common.by import By


def get_cookie_expiry_value(webdriver):
    cookies = webdriver.get_cookies()
    print(cookies)
    return int(cookies[0].get('expiry'))


max_expiry = 0
top_secret = ''

with webdriver.Chrome() as webdriver:
    webdriver.get('https://parsinger.ru/methods/5/index.html')

    # cookie_dict = webdriver.get_cookies()
    # secret_cookies_values = [int(cookie['value']) for cookie in cookie_dict if
    #                          (int(cookie.get('name').split('_')[-1]) % 2 == 0 and cookie.get('name').startswith(
    #                              'secret_cookie'))]

    urls = webdriver.find_elements(By.CSS_SELECTOR, 'div.urls a')

    for url in urls:
        url.click()
        secret_number = webdriver.find_element(By.ID, 'result').text
        expiry = get_cookie_expiry_value(webdriver)
        if max_expiry < expiry:
            max_expiry = expiry
            max_expiry_link = url
            top_secret = secret_number
        webdriver.back()

    # pprint(cookie_dict)
    # pprint(secret_cookies_values)
    print(max_expiry, top_secret)
