import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

url = "https://parsinger.ru/selenium/5.10/2/index.html"

with webdriver.Chrome() as driver:
    driver.implicitly_wait(10)
    driver.get(url)

    # Находим элементы
    # By.CSS_SELECTOR, ".draganddrop"
    # elements = driver.find_elements(By.CSS_SELECTOR, '.draganddrop.ui-draggable.ui-draggable-handle')
    # elements = driver.find_elements('div, {'class': ['text', 'highlight']})

    draggables = driver.find_elements(By.XPATH, '//div[contains(@class,"draganddrop")]')
    draganddrop_end = driver.find_element(By.CLASS_NAME, "draganddrop_end")
    ac = ActionChains(driver)
    # Выполняем перетаскивания
    for draggable in draggables:
        time.sleep(0.5)
        ac.drag_and_drop(draggable, draganddrop_end).perform()

    result = driver.find_element(By.ID, "message")
    WebDriverWait(driver, poll_frequency=0.1, timeout=10).until(lambda x: result.text != '')
    print(result.text)

