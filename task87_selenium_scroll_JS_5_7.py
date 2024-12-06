import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException
import sympy as sp

option = webdriver.ChromeOptions()
# option.add_argument('--headless')
results = []

with webdriver.Chrome(options=option) as browser:
    browser.get('https://parsinger.ru/scroll/4/index.html')
    buttons = browser.find_element(By.CLASS_NAME, 'main').find_elements(By.CLASS_NAME, 'btn')
    time.sleep(0.1)
    print(len(buttons))
    for button in buttons:
        try:
            button.click()
            print(button.text, browser.find_element(By.ID, 'result').text)
        except ElementClickInterceptedException as e:
            browser.execute_script("return arguments[0].scrollIntoView(true);", button)
            button.click()
            print(button.text, browser.find_element(By.ID, 'result').text, 'Blocked')
        results.append(browser.find_element(By.ID, 'result').text)

    time.sleep(0.1)
    results = list(map(int, results))
    print(results, len(results), sum(results))


