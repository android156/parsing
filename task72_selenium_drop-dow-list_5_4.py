import time
from random import randint
from selenium import webdriver
from selenium.webdriver.common.by import By
import faker

fake = faker.Faker('ru_RU')

with webdriver.Chrome() as browser:
    browser.get('http://parsinger.ru/selenium/7/7.html')
    drop_down_list = browser.find_elements(By.TAG_NAME, 'option')

    result = sum([int(el.text) for el in drop_down_list])
    browser.find_element(By.ID, 'input_result').send_keys(str(result))
    browser.find_element(By.CLASS_NAME, 'btn').click()
    element = browser.find_element(By.ID, 'result').text
    print(element)
