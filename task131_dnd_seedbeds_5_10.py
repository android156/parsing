from selenium import webdriver
from selenium.common import ElementClickInterceptedException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options

options = Options()
options.headless = True
# Установите предпочтительное разрешение окна
options.add_argument("--window-size=1920,1080")# Можно поиграть с размерами и поставить их больше



url = "https://parsinger.ru/selenium/5.10/8/index.html"

with webdriver.Chrome(options=options) as browser:
    browser.get(url)

    # Ожидаем загрузки всех квадратов и рамок
    pieces = WebDriverWait(browser, poll_frequency=0.1, timeout=10).until(
        EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "#pieces_container > div")))
    seedbeds = WebDriverWait(browser, poll_frequency=0.1, timeout=10).until(
        EC.visibility_of_all_elements_located((By.CLASS_NAME, "ui-droppable")))

    ac = ActionChains(browser)

    # Перетаскиваем квадраты в рамки

    for i, piece in enumerate(pieces):

        piece_x_offset = int(piece.get_attribute('id').split('_')[1]) + i * 5
        piece_y_offset = piece.location['y']
        try:
            ac.drag_and_drop_by_offset(piece, piece_x_offset, piece_y_offset).perform()
        except ElementClickInterceptedException:
            print("Ошибка: не удалось выполнить перетаскивание. Повторная попытка.")

    # Ждем появления сообщения о завершении задачи
    WebDriverWait(browser, poll_frequency=0.1, timeout=30).until(
        EC.text_to_be_present_in_element((By.ID, "message"), '')
    )
    print(browser.find_element(By.ID, "message").text)

