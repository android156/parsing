import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

url = "https://parsinger.ru/selenium/5.10/1/index.html"

with webdriver.Chrome() as driver:
    driver.get(url)
    time.sleep(2)

    # Находим элементы
    draganddrop = driver.find_element(By.CLASS_NAME, "draganddrop")
    draganddrop_end = driver.find_element(By.CLASS_NAME, "draganddrop_end")

    # Выполняем перетаскивание
    ActionChains(driver).drag_and_drop(draganddrop, draganddrop_end).perform()
    time.sleep(2)

    # *******************************************************************************************

    url = "https://parsinger.ru/selenium/5.10/5/index.html"

    driver.get(url)
    slider = driver.find_element(By.ID, "volume")
    time.sleep(2)

    ActionChains(driver).click_and_hold(slider).move_by_offset(50, 0).release().perform()

    time.sleep(2)

    # *******************************************************************************************

    driver.get("https://parsinger.ru/selenium/5.10/7/index.html")
    element_to_drag = driver.find_element(By.ID, "click_and_hold")
    time.sleep(1)
    # Создание объекта ActionChains, инициализация операции перетаскивания элемента на 500 пикселей вправо
    # и выполнение цепочки действий
    ActionChains(driver).drag_and_drop_by_offset(element_to_drag, 500, 0).release().perform()

    time.sleep(2)
    # *******************************************************************************************
    url = "https://parsinger.ru/selenium/5.10/7/index.html"
    # Устанавливаем неявное ожидание для всех элементов
    driver.implicitly_wait(10)

    # Переход на страницу
    driver.get(url)
    time.sleep(1)
    # Поиск элемента для перетаскивания и контейнера
    click_and_hold_element = driver.find_element(By.ID, "click_and_hold")
    container = driver.find_element(By.CLASS_NAME, "container")

    # Выполнение операции перетаскивания
    actions = ActionChains(driver)
    actions.click_and_hold(click_and_hold_element).move_to_element(container).release().perform()

    # Даем время для визуальной проверки (по желанию)
    time.sleep(5)

    # Ожидание загрузки элементов (10 секунд)
    driver.implicitly_wait(10)

    # Открытие локальной HTML страницы
    driver.get("https://parsinger.ru/selenium/5.10/9/index.html")

    # Поиск элемента (квадрата) на странице
    square = driver.find_element(By.CSS_SELECTOR, "canvas")

    # Создание объекта ActionChains для выполнения действий с элементами
    actions = ActionChains(driver)

    # Передвижение квадрата на указанные координаты
    actions.click_and_hold(square).move_by_offset(100, -100).release().perform()

    # Пауза для визуальной проверки результата
    time.sleep(5)