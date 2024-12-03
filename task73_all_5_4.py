import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import sympy as sp

option = webdriver.ChromeOptions()
# option.add_argument('--headless')

with webdriver.Chrome(options=option) as browser:
    browser.get('https://parsinger.ru/selenium/6/6.html')
    exp = browser.find_element(By.ID, 'text_box').text
    res_exp = sp.sympify(exp)
    dd_list = browser.find_element(By.ID, 'selectId')
    [el.click() for el in dd_list.find_elements(By.XPATH, './*') if int(el.text) == res_exp]
    # dd_list.send_keys(str(res_exp))
    time.sleep(0.5)
    browser.find_element(By.CLASS_NAME, 'btn').click()
    res = browser.find_element(By.ID, 'result').text
    time.sleep(0.5)
    # exp_parts = browser.find_elements(By.ID, 'input_result').send_keys(str(result))
    # drop_down_list = browser.find_elements(By.TAG_NAME, 'option')
    #
    # result = sum([int(el.text) for el in drop_down_list])
    # browser.find_element(By.ID, 'input_result').send_keys(str(result))
    # browser.find_element(By.CLASS_NAME, 'btn').click()
    # element = browser.find_element(By.ID, 'result').text
    print(res)
