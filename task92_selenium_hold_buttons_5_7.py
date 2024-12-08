import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/5.7/5/index.html')
    actions = ActionChains(browser)
    buttons = browser.find_elements(By.CLASS_NAME, 'timer_button')
    for button in buttons:
        hold_time = float(button.get_attribute('value'))
        actions.click_and_hold(button).pause(hold_time).release(button).perform()
    time.sleep(1)
    alert = browser.switch_to.alert
    print(alert.text)
    alert.accept()