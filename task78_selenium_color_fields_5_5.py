import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import sympy as sp

option = webdriver.ChromeOptions()
# option.add_argument('--headless')

with webdriver.Chrome(options=option) as browser:
    browser.get('https://parsinger.ru/selenium/5.5/4/1.html')
    parents = browser.find_elements(By.CLASS_NAME, 'parent')
    for parent in parents:
        grey_el = parent.find_element(By.CSS_SELECTOR, 'textarea[color="gray"]')
        blue_el = parent.find_element(By.CSS_SELECTOR, 'textarea[color="blue"]')
        blue_el.send_keys(grey_el.text)
        grey_el.clear()
        time.sleep(0.05)
        parent.find_element(By.TAG_NAME, 'button').click()
    browser.find_element(By.ID, 'checkAll').click()
    time.sleep(1)
    print(browser.find_element(By.ID, 'congrats').text)

# <p id="congrats">FGFF-D546-DF31-34SQ-4346-93PF</p>
