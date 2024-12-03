import time
from random import randint
from selenium import webdriver
from selenium.webdriver.common.by import By
import faker

options_chrome = webdriver.ChromeOptions()
options_chrome.add_argument('--headless')
options_chrome.add_argument('--disable-gpu')

with webdriver.Chrome(options=options_chrome) as browser:
    browser.get('http://parsinger.ru/selenium/3/3.html')
    p_elements = browser.find_elements(By.TAG_NAME, 'p')
    print(sum([int(p.text) for p in p_elements]))


