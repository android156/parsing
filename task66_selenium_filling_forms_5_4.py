import time
from random import randint
from selenium import webdriver
from selenium.webdriver.common.by import By
import faker

fake = faker.Faker('ru_RU')

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/1/1.html')
    input_forms = browser.find_elements(By.CLASS_NAME, 'form')
    form_list = [fake.first_name_male(), fake.last_name_male(), fake.middle_name_male(), randint(10, 99),
                 fake.city_name(), fake.email()]
    for i, input_form in enumerate(input_forms):
        input_form.send_keys(form_list[i])
    browser.find_element(By.ID, "btn").click()
    time.sleep(5)

