import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

total = 0
with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/infiniti_scroll_3/')
    actions = ActionChains(browser)
    time.sleep(1)
    main_divs = browser.find_elements(By.CSS_SELECTOR, 'div.main > div')
    print(len(main_divs))
    for div in main_divs:
        while True:
            last_span = div.find_element(By.CSS_SELECTOR, 'div span:last-child')
            browser.execute_script('return arguments[0].scrollIntoView(true);', last_span)
            time.sleep(0.1)
            if last_span.get_attribute('class') == 'last-of-list':
                break
        total += sum(int(span.text) for span in div.find_elements(By.CSS_SELECTOR, 'div > span'))
    print(total)

# scrolls = driver.find_elements(By.CSS_SELECTOR, '[class^="scroll-container"]')
# total += int(driver.find_element(By.XPATH, '//span[contains(@id,"result")]').text)

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
