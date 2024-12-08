import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

total = 0
processed_items = []

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/infiniti_scroll_1/')
    actions = ActionChains(browser)
    time.sleep(0.5)
    main_div = browser.find_element(By.CSS_SELECTOR, 'div#scroll-container')
    while True:
        spans = main_div.find_elements(By.TAG_NAME, 'span')
        checkboxes = main_div.find_elements(By.TAG_NAME, 'input')
        for span, checkbox in zip(spans, checkboxes):
            if (span, checkbox) not in processed_items:
                print(span.text)
                total += int(span.text)
                checkbox.click()
                checkbox.send_keys(Keys.TAB)
                time.sleep(0.1)
                processed_items.append((span, checkbox))

                if span.get_attribute('class') == 'last-of-list':
                    break
        else:
            continue
        break

print(total)

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