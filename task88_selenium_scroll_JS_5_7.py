import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from math import ceil
from selenium.common.exceptions import ElementClickInterceptedException
import sympy as sp

option = webdriver.ChromeOptions()
# option.add_argument('--headless')
results = []

with webdriver.Chrome(options=option) as browser:
    browser.get('https://parsinger.ru/selenium/5.7/1/index.html')
    window_height = browser.execute_script("return window.innerHeight")
    full_height = browser.execute_script("return document.body.scrollHeight")
    num_screens = (full_height / window_height).__ceil__()
    print(full_height, window_height, num_screens)
    current_scroll = 0
    for i_screen in range(num_screens):
        browser.execute_script(f"window.scrollBy(0,{i_screen * window_height})")
        buttons = browser.find_elements(By.CLASS_NAME, 'clickMe')
        [(button.click(), print('click!')) for button in buttons]



        # try:
        #     button.click()
        #     print(button.text, browser.find_element(By.ID, 'result').text)
        # except ElementClickInterceptedException as e:
        #     browser.execute_script("return arguments[0].scrollIntoView(true);", button)
        #     button.click()
        #     print(button.text, browser.find_element(By.ID, 'result').text, 'Blocked')
        # results.append(browser.find_element(By.ID, 'result').text)

    time.sleep(5)
    print(browser.switch_to.alert.text)



# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time
#
# driver = webdriver.Chrome()  # или любой другой драйвер, который у вас установлен
# driver.get('https://parsinger.ru/selenium/5.7/1/index.html')  # замените на URL вашего сайта
#
# # Находим все кнопки на странице
# buttons = driver.find_elements(By.CLASS_NAME, "clickMe")
# time.sleep(1)
#
# count = 0
# for button in buttons:
#     # Прокрутка до кнопки
#     driver.execute_script("return arguments[0].scrollIntoView(true);", button)
#     # time.sleep(.2)  # Пауза для уверенности, что страница прокрутилась и элемент видим
#     button.click()  # Нажимаем на кнопку
#     count += 1
#
#
# wait = WebDriverWait(driver, 10)
# alert = wait.until(EC.alert_is_present())
# alert_text = alert.text
# alert.accept()

# print(alert_text)
# print(count)