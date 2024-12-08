from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

# driver = ... # инициализация драйвера
# ActionChains(driver).key_down(Keys.SHIFT).send_keys("abc").perform()
#
# ActionChains(driver).key_down(Keys.SHIFT).send_keys("a").key_up(Keys.SHIFT).send_keys("b").perform()

import time
from selenium.webdriver import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('http://parsinger.ru/scroll/1/')
    browser.find_element(By.TAG_NAME, 'input').send_keys(Keys.TAB)
    time.sleep(2)

    tags_input = browser.find_elements(By.TAG_NAME, 'input')
    for input in tags_input[:3]:
        input.send_keys(Keys.DOWN)
        time.sleep(1)

    browser.get(r"https://parsinger.ru/selenium/5.7/3/test/index.html")

    list_input = []      # Инициализируем пустой список для хранения обработанных элементов ввода
    while True:          # Начинаем бесконечный цикл

        # Ищем все элементы input на веб-странице и добавляем их в список input_tags
        input_tags = browser.find_elements(By.TAG_NAME, 'input')

        # Обходим каждый элемент input в списке
        for tag_input in input_tags:
            # Проверяем, не обрабатывали ли мы уже этот элемент ранее
            if tag_input not in list_input:
                tag_input.send_keys(Keys.DOWN)     # Отправляем клавишу "Вниз"
                browser.execute_script("return arguments[0].scrollIntoView(true);", tag_input)
                tag_input.click()                  # Кликаем на элемент
                list_input.append(tag_input)       # Добавляем элемент в список обработанных элементов

#
# ADD 	ALT 	ARROW_DOWN
# ARROW_LEFT 	ARROW_RIGHT 	ARROW_UP
# BACKSPACE 	BACK_SPACE 	CANCEL
# CLEAR 	COMMAND 	CONTROL
# DECIMAL 	DELETE 	DIVIDE
# DOWN 	UP 	ENTER
# EQUALS 	ESCAPE 	F1
# F10 	F11 	F12
# F2 	F3 	F4
# F5 	F6 	F7
# F8 	F9 	HELP
# HOME 	INSERT 	LEFT
# LEFT_ALT 	LEFT_CONTROL 	LEFT_SHIFT
# META 	MULTIPLY 	NULL
# NUMPAD0 	NUMPAD1 	NUMPAD2
# NUMPAD3 	NUMPAD4 	NUMPAD5
# NUMPAD6 	NUMPAD7 	NUMPAD8
# NUMPAD9 	PAGE_DOWN 	PAGE_UP
# PAUSE 	RETURN 	RIGHT
# SEMICOLON 	SEPARATOR 	SHIFT
# SPACE 	SUBTRACT
#
# TAB
# END
#