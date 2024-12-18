import time

from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('https://yandex.ru/maps/2/saint-petersburg/?ll=30.314997%2C59.938784&z=11')

    placeholder = browser.find_element(By.CSS_SELECTOR, '[placeholder]')
    placeholder.send_keys('Эрмитаж')

    find_button = browser.find_element(By.CSS_SELECTOR, '[aria-label="Найти"]')
    find_button.click()

    time.sleep(10)

