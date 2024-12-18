import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import pyperclip

with (webdriver.Chrome() as browser):
    browser.get('https://parsinger.ru/selenium/5.8/3/index.html')
    check_button = browser.find_element(By.CSS_SELECTOR, 'input#check')
    pins = browser.find_elements(By.CSS_SELECTOR, 'span.pin')
    for pin in pins:
        extracted_text = pin.text
        check_button.click()
        # time.sleep(0.1)
        prompt = browser.switch_to.alert
        prompt.send_keys(extracted_text)
        prompt.accept()
        result = browser.find_element(By.CSS_SELECTOR, 'p#result').text
        if not result == 'Неверный пин-код':
            pyperclip.copy(result)
            print(result)
            break
        


