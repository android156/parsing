import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import pyperclip

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/5.8/1/index.html')
    btns = browser.find_elements(By.CSS_SELECTOR, 'input.buttons')
    for btn in btns:
        btn.click()
        time.sleep(0.1)
        browser.switch_to.alert.accept()
        result = browser.find_element(By.CSS_SELECTOR, 'p#result').text
        if not result == '':
            pyperclip.copy(result)
            print(result)
            break


