import time
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('http://parsinger.ru/blank/modal/1/index.html')
    browser.find_element(By.ID, 'alert').click()
    time.sleep(1)
    alert = browser.switch_to.alert # Если вы планируете что-то делать с этим событием, можно добавить его в переменную
    print(alert.text)
    time.sleep(1)
    alert.accept()
    time.sleep(3)

    browser.find_element(By.ID, 'prompt').click()
    time.sleep(2)
    prompt = browser.switch_to.alert
    time.sleep(1)
    prompt.send_keys('Введёный текст')
    time.sleep(1)
    prompt.accept()
    time.sleep(.5)
    print(browser.find_element(By.ID, 'result').text)
    time.sleep(3)

    browser.get('http://parsinger.ru/blank/modal/1/index.html')
    browser.find_element(By.ID, 'confirm').click()
    time.sleep(2)
    prompt = browser.switch_to.alert
    prompt.accept() #Замените на .dismiss() чтобы нажать на кнопку "Отмена"
    time.sleep(3)