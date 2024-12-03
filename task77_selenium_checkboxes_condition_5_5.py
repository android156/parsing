import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import sympy as sp

option = webdriver.ChromeOptions()
# option.add_argument('--headless')

with webdriver.Chrome(options=option) as browser:
    browser.get('https://parsinger.ru/selenium/5.5/3/1.html')
    parents = browser.find_elements(By.CLASS_NAME, 'parent')
    print(sum([int(parent.find_element(By.TAG_NAME, 'textarea').text) for parent in parents if
               parent.find_element(By.CLASS_NAME, 'checkbox').is_selected()]))
