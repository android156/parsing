import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

url = "https://parsinger.ru/draganddrop/1/index.html"

with webdriver.Chrome() as driver:
    driver.implicitly_wait(10)
    driver.get(url)

    # Находим элементы
    draggable = driver.find_element(By.CSS_SELECTOR, "#draggable")
    draganddrop_end = driver.find_element(By.CSS_SELECTOR, "#field2")

    # Выполняем перетаскивание
    ActionChains(driver).drag_and_drop(draggable, draganddrop_end).perform()
    result = driver.find_element(By.ID, "result")
    WebDriverWait(driver, poll_frequency=0.1, timeout=10).until(lambda x: result.text != '')
    print(result.text)

