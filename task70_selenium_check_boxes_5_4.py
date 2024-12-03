import time
from random import randint
from selenium import webdriver
from selenium.webdriver.common.by import By
import faker

fake = faker.Faker('ru_RU')

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/4/4.html')
    checkboxes = browser.find_elements(By.CLASS_NAME, 'check')
    [ch_b.click() for ch_b in checkboxes]
    browser.find_element(By.CLASS_NAME, 'btn').click()
    element = browser.find_element(By.ID, 'result').text
    print(element)
    time.sleep(1)

