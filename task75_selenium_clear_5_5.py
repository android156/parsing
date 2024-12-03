import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import sympy as sp

option = webdriver.ChromeOptions()
# option.add_argument('--headless')

with webdriver.Chrome(options=option) as browser:
    browser.get('https://parsinger.ru/selenium/5.5/1/1.html')
    # fields = browser.find_elements(By.CLASS_NAME, 'text-field')
    el_list = browser.find_element(By.ID, 'textfields-container')
    [el.clear() for el in el_list.find_elements(By.XPATH, './*')]

    time.sleep(0.1)
    browser.find_element(By.ID, 'checkButton').click()
    # Переключаемся на алерт
    alert = browser.switch_to.alert
    # Получаем текст с алерта
    alert_text = alert.text
    print(alert_text)
    time.sleep(2)
    browser.switch_to.alert.accept()
    time.sleep(2)

