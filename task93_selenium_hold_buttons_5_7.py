import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/scroll/2/index.html')
    actions = ActionChains(browser)

    checkboxes = browser.find_elements(By.CLASS_NAME, 'checkbox_class')
    for chb in checkboxes:
        chb.click()
        chb.send_keys(Keys.DOWN)
    time.sleep(1)

    divs_lorem = browser.find_elements(By.CLASS_NAME, 'lorem')

    spans = [div.find_element(By.CSS_SELECTOR, 'p > span').text for div in divs_lorem]
    numbers = [int(span) for span in spans if span.isnumeric()]
    print(sum(numbers))

    # total += int(driver.find_element(By.XPATH, '//span[contains(@id,"result")]').text)

