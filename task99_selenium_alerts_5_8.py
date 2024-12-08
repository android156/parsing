import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

total = 0
processed_items = []

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/5.7/4/index.html')
    actions = ActionChains(browser)
    time.sleep(0.5)
    main_div = browser.find_element(By.CSS_SELECTOR, 'div#main_container')
    num_children = 0
    children = []
    while True:
        last_child = main_div.find_element(By.CSS_SELECTOR, 'div.child_container:last-child')
        browser.execute_script('return arguments[0].scrollIntoView(true);', last_child)
        time.sleep(0.1)
        children = main_div.find_elements(By.CSS_SELECTOR, 'div.child_container')
        if len(children) == num_children:
            break
        num_children = len(children)
    time.sleep(1)
    for child in children:
        checkboxes = child.find_elements(By.TAG_NAME, 'input')
        for checkbox in checkboxes:
            if int(checkbox.get_attribute('value')) % 2 == 0:
                checkbox.click()
    time.sleep(1)
    browser.find_element(By.CLASS_NAME, 'alert_button').click()
    time.sleep(0.1)
    alert = browser.switch_to.alert
    print(alert.text)
    alert.accept()


# child_cont = child_cont.find_element(By.XPATH, 'following-sibling::div[@class="child_container"]')


# from selenium.webdriver import ActionChains
# from selenium.webdriver.common.by import By
# from selenium import webdriver
#
# with webdriver.Chrome() as browser:
#     browser.get("https://parsinger.ru/selenium/5.7/4/index.html")
#     child_cont = browser.find_element(By.CSS_SELECTOR, 'div.child_container')
#     while True:
#         ActionChains(browser).scroll_to_element(child_cont).perform()
#         elements = child_cont.find_elements(By.TAG_NAME, 'input')
#         for checkbox in elements:
#             if not int(checkbox.get_attribute("value")) % 2:
#                 checkbox.click()
#         try:
#             # поиск следующего элемента для скроллинга к нему на следующей итерации
#             child_cont = child_cont.find_element(By.XPATH, 'following-sibling::div[@class="child_container"]')
#         except:
#             break # Когда элементы кончатся, выходим из цикла
#     alert_button = browser.find_element(By.CSS_SELECTOR, ".alert_button")
#     ActionChains(browser).scroll_to_element(alert_button).perform()
#     alert_button.click()
#     print(browser.switch_to.alert.text)
#