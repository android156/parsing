import time

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from fake_useragent import UserAgent

# # Генерация случайного user-agent
# ua = UserAgent()
# user_agent = ua.random
# print(f"Используемый User-Agent: {user_agent}")

options_chrome = webdriver.ChromeOptions()
options_chrome.add_argument('--disable-notifications')
options_chrome.add_argument('--headless')
# # Отключение автоматизации
# options_chrome.add_experimental_option("excludeSwitches", ["enable-automation"])
# options_chrome.add_experimental_option("useAutomationExtension", False)
# # Установка дополнительных аргументов
# options_chrome.add_argument("--disable-blink-features=AutomationControlled")

# options_chrome.add_argument(f"user-agent={user_agent}")

nes_clear_window_height = 555
nes_clear_window_width = 555


def get_clear_window_dimensions(browser):
    clear_dimensions = (browser.execute_script
                        ("""
                            return {
                                width: window.innerWidth,
                                height: window.innerHeight
                            };
                        """))
    return clear_dimensions['width'], clear_dimensions['height']


def get_full_window_dimensions(browser):
    dimensions = browser.get_window_size()
    return dimensions['width'], dimensions['height']


with webdriver.Chrome(options=options_chrome) as browser:
    # Загрузка указанного URL ('http://parsinger.ru/window_size/1/') в открытом окне браузера.
    browser.get('http://parsinger.ru/window_size/1/')

    # Получаем реальные размеры области без рамок
    clear_width, clear_height = get_clear_window_dimensions(browser)
    print(clear_width, clear_height, ' - Реальные размеры текущего окна без рамок')

    # Получаем полные размеры окна с рамками и меню
    width, height = get_full_window_dimensions(browser)
    print(width, height, ' - Полные размеры текущего окна с рамками')

    # Установка размера окна браузера.
    browser.set_window_size(width - clear_width + nes_clear_window_width, height - clear_height + nes_clear_window_height)

    # Получение текущего размера окна браузера и вывод его размеров: ширина, высота
    print(get_full_window_dimensions(browser), ' - Полные размеры измененного окна с рамками')
    # Получение текущего размера окна браузера без рамок и вывод его размеров: ширина, высота
    print(get_clear_window_dimensions(browser), ' - Реальные размеры измененного окна без рамок')
    time.sleep(0.1)
    try:
        result = browser.find_element(By.ID, "result").text
        print(result)
    except NoSuchElementException:
        print('Элемент не обнаружен')
