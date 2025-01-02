import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/expectations/6/index.html')
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.ID, "btn"))).click()
    element = WebDriverWait(browser, poll_frequency=0.1, timeout=30).until(
        EC.presence_of_element_located((By.CLASS_NAME, "BMH21YY")))
    print(element.text)

# Вместе с верхним не применять
# driver.implicitly_wait(2)
# driver.get('https://www.selenium.dev/selenium/web/dynamic.html')
# driver.find_element(By.ID, "adder").click()
# added = driver.find_element(By.ID, "box0")
