import time
from random import randint
from selenium import webdriver
from selenium.webdriver.common.by import By
import faker

fake = faker.Faker('ru_RU')

with webdriver.Chrome() as browser:
    browser.get('http://parsinger.ru/selenium/2/2.html')
    link = browser.find_element(By.PARTIAL_LINK_TEXT, '16243162441624')
    link.click()
    element = browser.find_element(By.ID, 'result').text
    print(element)
    time.sleep(5)

