import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import sympy as sp

option = webdriver.ChromeOptions()
# option.add_argument('--headless')

with webdriver.Chrome(options=option) as browser:
    browser.get('https://parsinger.ru/methods/1/index.html')
    while (res := browser.find_element(By.ID, 'result').text).isdecimal() is not True:
        browser.refresh()
    print(res)
    time.sleep(5)
    # exp_parts = browser.find_elements(By.ID, 'input_result').send_keys(str(result))
    # drop_down_list = browser.find_elements(By.TAG_NAME, 'option')
    #
    # result = sum([int(el.text) for el in drop_down_list])
    # browser.find_element(By.ID, 'input_result').send_keys(str(result))
    # browser.find_element(By.CLASS_NAME, 'btn').click()
    # element = browser.find_element(By.ID, 'result').text

