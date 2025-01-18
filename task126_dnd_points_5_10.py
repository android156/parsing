import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

url = "https://parsinger.ru/draganddrop/3/index.html"

with webdriver.Chrome() as driver:
    driver.implicitly_wait(10)
    driver.get(url)

    # Находим элементы

    points = driver.find_elements(By.CLASS_NAME, "controlPoint")
    draggable = driver.find_element(By.CSS_SELECTOR, "#block1")
    ac = ActionChains(driver).click_and_hold(draggable)

    # Выполняем перетаскивание
    for point in points:
        ac.move_to_element(point)
    ac.perform()

    result = driver.find_element(By.ID, "message")
    WebDriverWait(driver, poll_frequency=0.1, timeout=10).until(lambda x: result.text != '')
    print(result.text)

