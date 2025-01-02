import time

from selenium import webdriver
from selenium.common import UnexpectedAlertPresentException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/5.9/6/index.html')
    checkbox = browser.find_element(By.CSS_SELECTOR, '#myCheckbox')
    # Ждем пока checkbox не станет selected

    WebDriverWait(browser, poll_frequency=0.1, timeout=10).until(EC.element_to_be_selected(checkbox))
    WebDriverWait(browser, poll_frequency=0.1, timeout=10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '#main_container > button'))).click()
    code = browser.find_element(By.CSS_SELECTOR, '#result').text
    print(code)

# Нажатие на кнопку "Нажми на меня"
# button = driver.find_element(By.CSS_SELECTOR, "button[onclick='showSecretNumber()']")
# button.click()

# def text_is_not_empty(driver):
#     element = driver.find_element(*button_locator)
#     return element.text != ''
#
# wait.until(text_is_not_empty)