import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import pyperclip

with (webdriver.Chrome() as browser):
    browser.get('https://parsinger.ru/selenium/5.8/2/index.html')
    main_input = browser.find_element(By.CSS_SELECTOR, 'input#input')
    check_button = browser.find_element(By.CSS_SELECTOR, 'input#check')
    btns = browser.find_elements(By.CSS_SELECTOR, 'input.buttons')
    for btn in btns:
        btn.click()
        time.sleep(0.01)
        alert = browser.switch_to.alert
        code = alert.text
        alert.accept()
        main_input.send_keys(code)
        check_button.click()
        result = browser.find_element(By.CSS_SELECTOR, 'p#result').text
        if not result == 'Неверный пин-код':
            pyperclip.copy(result)
            print(result)
            break



