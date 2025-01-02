import time

from selenium import webdriver
from selenium.common import UnexpectedAlertPresentException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

code_list = []

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/5.9/5/index.html')
    box_buttons = browser.find_elements(By.CSS_SELECTOR, 'div#main_container > div.box_button')
    # Ждем пока крестик на рекламе станет кликабельным (перестраховка)
    for button in box_buttons:
        button.click()
        ad_window = WebDriverWait(browser, poll_frequency=0.1, timeout=10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#ad_window'))
        )
        WebDriverWait(browser, poll_frequency=0.1, timeout=10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button#close_ad'))).click()
        # Ждем пока реклама не исчезнет и не откроетcя кусок кода
        WebDriverWait(browser, poll_frequency=0.1, timeout=10).until(EC.invisibility_of_element_located(ad_window))
        # Ждем пока текст проявится
        WebDriverWait(browser, poll_frequency=0.1, timeout=10).until(lambda x: button.text != '')
        code_list.append(button.text)

    print('-'.join(code_list))

# Нажатие на кнопку "Нажми на меня"
# button = driver.find_element(By.CSS_SELECTOR, "button[onclick='showSecretNumber()']")
# button.click()

# def text_is_not_empty(driver):
#     element = driver.find_element(*button_locator)
#     return element.text != ''
#
# wait.until(text_is_not_empty)