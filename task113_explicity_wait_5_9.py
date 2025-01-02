import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

with webdriver.Chrome() as browser:
    browser.get('http://parsinger.ru/expectations/3/index.html')
    element = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.ID, "btn"))).click()
    WebDriverWait(browser, poll_frequency=0.5, timeout=100).until(EC.title_is('345FDG3245SFD'))
    print(browser.find_element(By.ID, 'result').text)


# Вместе с верхним не применять
# driver.implicitly_wait(2)
# driver.get('https://www.selenium.dev/selenium/web/dynamic.html')
# driver.find_element(By.ID, "adder").click()
# added = driver.find_element(By.ID, "box0")