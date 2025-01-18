import time
from selenium import webdriver
from selenium.common import ElementClickInterceptedException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import webcolors


def get_color_from_obj_style(obj):
    """
    Получает цвет из атрибута style объекта.
    """
    style = obj.get_attribute('style')
    styles_list = style.split(';')
    for st in styles_list:
        if 'color' in st:
            color_string = st.strip().split(':')[1].strip()
            if color_string.startswith('rgb'):
                return color_string
            return f'rgb{tuple(webcolors.name_to_rgb(color_string))}'


url = "https://parsinger.ru/selenium/5.10/3/index.html"

with webdriver.Chrome() as browser:
    browser.get(url)

    # Ожидаем загрузки всех квадратов и рамок
    squares = WebDriverWait(browser, poll_frequency=0.1, timeout=10).until(
        EC.visibility_of_all_elements_located((By.CLASS_NAME, "draganddrop")))
    frames = WebDriverWait(browser, poll_frequency=0.1, timeout=10).until(
        EC.visibility_of_all_elements_located((By.CLASS_NAME, "draganddrop_end")))

    ac = ActionChains(browser)

    # Перетаскиваем квадраты в рамки
    while squares and frames:
        for square in squares[:]:  # Используем копию списка для безопасного удаления
            square_color = get_color_from_obj_style(square)
            for frame in frames[:]:  # Используем копию списка для безопасного удаления
                frame_color = get_color_from_obj_style(frame)

                if frame_color == square_color:
                    try:
                        ac.drag_and_drop(square, frame).perform()
                        frames.remove(frame)  # Удаляем рамку из списка
                        squares.remove(square)  # Удаляем квадрат из списка
                        break
                    except ElementClickInterceptedException:
                        print("Ошибка: не удалось выполнить перетаскивание. Повторная попытка.")
            else:
                print(f'Подходящий цвет для квадрата {square_color} не найден.')

    # Ждем появления сообщения о завершении задачи
    result = WebDriverWait(browser, poll_frequency=0.1, timeout=30).until(
        EC.text_to_be_present_in_element((By.ID, "message"), '')
    )
    print(browser.find_element(By.ID, "message").text)

    time.sleep(5)