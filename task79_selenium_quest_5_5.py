import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import sympy as sp

option = webdriver.ChromeOptions()
# option.add_argument('--headless')

with webdriver.Chrome(options=option) as browser:
    browser.get('https://parsinger.ru/selenium/5.5/5/1.html')
    divs = browser.find_element(By.ID, 'main-container').find_elements(By.XPATH, './*')
    for div in divs:
        color = div.find_element(By.TAG_NAME, 'span').text
        [option.click() for option in div.find_elements(By.TAG_NAME, 'option') if
         option.get_attribute('value') == color]
        [button.click() for button in div.find_elements(By.TAG_NAME, 'button') if
         button.get_attribute('data-hex') == color]
        inputs = div.find_elements(By.TAG_NAME, 'input')
        inputs[0].click()
        inputs[1].send_keys(color)
        div.find_elements(By.TAG_NAME, 'button')[-1].click()
        # check_button = div.find_element(By.XPATH, ".//button[text()='Проверить']")
    browser.find_elements(By.TAG_NAME, 'button')[-1].click()
    # check_all_button = driver.find_element(By.XPATH, "//button[text()='Проверить все элементы']")
    alert = browser.switch_to.alert
    # Получаем текст с алерта
    alert_text = alert.text
    print(alert_text)
    time.sleep(2)
    alert.accept()
    time.sleep(2)


