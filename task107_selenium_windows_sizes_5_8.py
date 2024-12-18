import time

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from fake_useragent import UserAgent
import itertools


window_size_x = [616, 648, 680, 701, 730, 750, 805, 820, 855, 890, 955, 1000]
window_size_y = [300, 330, 340, 388, 400, 421, 474, 505, 557, 600, 653, 1000]

options_chrome = webdriver.ChromeOptions()
# # Генерация случайного user-agent
# ua = UserAgent()
# user_agent = ua.random
# print(f"Используемый User-Agent: {user_agent}")
# options_chrome.add_argument(f"user-agent={user_agent}")

options_chrome.add_argument('--disable-notifications')
# options_chrome.add_argument('--headless')
# Отключение автоматизации
options_chrome.add_experimental_option("excludeSwitches", ["enable-automation"])
options_chrome.add_experimental_option("useAutomationExtension", False)
# Установка дополнительных аргументов
options_chrome.add_argument("--disable-blink-features=AutomationControlled")


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
    browser.get('http://parsinger.ru/window_size/2/index.html')

    # Получаем реальные размеры области без рамок
    clear_width, clear_height = get_clear_window_dimensions(browser)
    print(clear_width, clear_height, ' - Реальные размеры текущего окна без рамок')

    # Получаем полные размеры окна с рамками и меню
    width, height = get_full_window_dimensions(browser)
    print(width, height, ' - Полные размеры текущего окна с рамками')

    width_shift, height_shift = width - clear_width, height - clear_height

    for nes_clear_window_width, nes_clear_window_height in itertools.product(window_size_x, window_size_y):

        # Установка размера окна браузера.
        browser.set_window_size(width_shift + nes_clear_window_width,
                                height_shift + nes_clear_window_height)

        # Получение текущего размера окна браузера и вывод его размеров: ширина, высота
        print(get_full_window_dimensions(browser), ' - Полные размеры измененного окна с рамками')
        # Получение текущего размера окна браузера без рамок и вывод его размеров: ширина, высота
        print(get_clear_window_dimensions(browser), ' - Реальные размеры измененного окна без рамок')
        time.sleep(0)
        try:
            result = browser.find_element(By.ID, "result").text
            if result:
                print(result)
                break
        except NoSuchElementException:
            print('Элемент при таком размере окна не обнаружен')
