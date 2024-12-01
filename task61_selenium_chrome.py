import time
from selenium import webdriver
from selenium.webdriver.common.by import By

options_chrome = webdriver.ChromeOptions()
# запуск без окна
# options_chrome.add_argument('--headless')
# Добавляем расширение
options_chrome.add_extension(r"C:\Users\n_deg\AppData\Local\Google\Chrome\User Data\Default\Extensions\ololmadlpnbbagpkjhdomclggmfomhdg\1.0.0_0.crx")
# Добавляем свой профиль
options_chrome.add_argument(r'user-data-dir=C:\Users\n_deg\AppData\Local\Google\Chrome\User Data\Default')

with webdriver.Chrome(options=options_chrome) as browser:
    url = 'https://yandex.ru/'
    browser.get(url)
    time.sleep(10)
    a = browser.find_element(By.TAG_NAME, 'a')
    print(a.get_attribute('href'))





