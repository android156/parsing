import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/infiniti_scroll_2/')
    actions = ActionChains(browser)
    time.sleep(1)
    main_div = browser.find_element(By.CSS_SELECTOR, 'div#scroll-container')
    while True:
        last_p = main_div.find_element(By.CSS_SELECTOR, 'p:last-child')
        if last_p.get_attribute('class') == 'last-of-list':
            break
        ActionChains(browser).move_to_element(last_p).scroll_by_amount(1, 500).perform()
        time.sleep(0.1)
    print(sum(int(p.text) for p in browser.find_elements(By.CSS_SELECTOR, 'div#scroll-container p')))


# import time
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# with webdriver.Edge() as browser:
#     browser.get('https://parsinger.ru/infiniti_scroll_1/')
#     time.sleep(2)
#
#     while True:
#         last_span = browser.find_element(By.CSS_SELECTOR, 'div#scroll-container span:last-child')
#         browser.execute_script('return arguments[0].scrollIntoView(true);', last_span)
#         if last_span.get_attribute('class') == 'last-of-list':
#             break
#
#     print(sum(int(span.text) for span in browser.find_elements(By.CSS_SELECTOR, 'div#scroll-container span')))