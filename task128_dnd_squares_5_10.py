import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

url = "https://parsinger.ru/draganddrop/2/index.html"

with webdriver.Chrome() as driver:
    driver.get(url)

    draggable = driver.find_element(By.CSS_SELECTOR, "#draggable")
    draganddrop_ends = driver.find_elements(By.CLASS_NAME, "box")
    ac = ActionChains(driver)
    # Выполняем перетаскивания
    for draganddrop_end in draganddrop_ends:
        time.sleep(0.5)
        ac.drag_and_drop(draggable, draganddrop_end).perform()

    result = driver.find_element(By.ID, "message")
    WebDriverWait(driver, poll_frequency=0.1, timeout=10).until(lambda x: result.text != '')
    print(result.text)

