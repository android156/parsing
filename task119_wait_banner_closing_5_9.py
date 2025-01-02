import time

from selenium import webdriver
from selenium.common import UnexpectedAlertPresentException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/5.9/4/index.html')
    ad = browser.find_element(By.CSS_SELECTOR, 'div#ad')
    # Ждем пока крестик на рекламе станет кликабельным (перестраховка)
    WebDriverWait(browser, poll_frequency=0.1, timeout=10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'div#ad > span'))).click()
    # Ждем пока реклама не исчезнет и не откроет нам возможность нажать на кнопку
    WebDriverWait(browser, poll_frequency=0.1, timeout=10).until(EC.invisibility_of_element_located(ad))
    # Ждем пока кнопка не будет кликабельна
    WebDriverWait(browser, poll_frequency=0.1, timeout=10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.box > button'))).click()
    # Ждем пока не будет видим элемент с кодом
    code = WebDriverWait(browser, poll_frequency=0.1, timeout=10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '#message'))).text
    print(code)

# Нажатие на кнопку "Нажми на меня"
# button = driver.find_element(By.CSS_SELECTOR, "button[onclick='showSecretNumber()']")
# button.click()