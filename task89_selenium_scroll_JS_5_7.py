import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from tqdm import tqdm

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/5.7/1/index.html')
    time.sleep(1)

    for button in tqdm(browser.find_elements(By.CLASS_NAME, 'clickMe')):
        browser.execute_script("return arguments[0].scrollIntoView(true);", button)
        button.click()

    # Ждем 1 секунду появления алерта
    time.sleep(1)

    alert = browser.switch_to.alert
    print(alert.text)
    alert.accept()