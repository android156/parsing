from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/5.9/7/index.html')
    containers = WebDriverWait(browser, poll_frequency=0.1, timeout=10).until(
        EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "#main_container > div.container")))
    result = browser.find_element(By.ID, "result")
    for container in containers:
        checkbox = container.find_element(By.TAG_NAME, 'input')
        button = container.find_element(By.TAG_NAME, 'button')
        if not checkbox.is_selected():
            checkbox.send_keys(Keys.SPACE)
        button.click()
    print(result.text)

# # Дожидаемся, когда чекбокс станет выбранным
#         checkbox = container.find_element(By.CSS_SELECTOR, "input[type='checkbox']")
#         wait.until(EC.element_to_be_selected((checkbox)))
