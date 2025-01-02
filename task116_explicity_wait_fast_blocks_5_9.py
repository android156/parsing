from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/5.9/2/index.html')
    element = WebDriverWait(browser, poll_frequency=0.1, timeout=150).until(
        EC.presence_of_element_located((By.ID, "qQm9y1rk")))
    element.click()
    alert = browser.switch_to.alert
    alert.accept()
    print(alert.text)
# Вместе с верхним не применять
# driver.implicitly_wait(2)
# driver.get('https://www.selenium.dev/selenium/web/dynamic.html')
# driver.find_element(By.ID, "adder").click()
# added = driver.find_element(By.ID, "box0")
