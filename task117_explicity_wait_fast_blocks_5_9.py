import time

from selenium import webdriver
from selenium.common import UnexpectedAlertPresentException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

ids_to_find = ['xhkVEkgm', 'QCg2vOX7', '8KvuO5ja', 'CFoCZ3Ze', '8CiPCnNB', 'XuEMunrz', 'vmlzQ3gH', 'axhUiw2I',
               'jolHZqD1', 'ZM6Ms3tw', '25a2X14r', 'aOSMX9tb', 'YySk7Ze3', 'QQK13iyY', 'j7kD7uIR']

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/5.9/3/index.html')
    elements = WebDriverWait(browser, poll_frequency=0.1, timeout=150).until(
        EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "div#main_container > div.box")))
    try:
        [element.click() for element in elements if element.get_attribute('id') in ids_to_find]
    except UnexpectedAlertPresentException as e:
        print(e)
        


# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait
#
# with webdriver.Chrome() as browser:
#     ids_to_find = ['xhkVEkgm', 'QCg2vOX7', '8KvuO5ja', 'CFoCZ3Ze', '8CiPCnNB', 'XuEMunrz', 'vmlzQ3gH', 'axhUiw2I',
#                    'jolHZqD1', 'ZM6Ms3tw', '25a2X14r', 'aOSMX9tb', 'YySk7Ze3', 'QQK13iyY', 'j7kD7uIR']
#     browser.get('https://parsinger.ru/selenium/5.9/3/index.html')
#     for el in ids_to_find:
#         locator = (By.ID, el)
#         WebDriverWait(browser, 30).until(EC.visibility_of_element_located(locator)).click()
#     alert = browser.switch_to.alert
#     print(alert.text)
#     alert.accept()