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



url = "https://parsinger.ru/selenium/5.10/4/index.html"

with webdriver.Chrome(options=options) as browser:
    browser.get(url)

    # Ожидаем загрузки всех квадратов и рамок
    balls = WebDriverWait(browser, poll_frequency=0.1, timeout=10).until(
        EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".basket_with_toys > div")))
    baskets = WebDriverWait(browser, poll_frequency=0.1, timeout=10).until(
        EC.visibility_of_all_elements_located((By.CLASS_NAME, "ui-droppable")))

    ac = ActionChains(browser)

    # Перетаскиваем квадраты в рамки
    while balls:
        for ball in balls[:]:  # Используем копию списка для безопасного удаления
            ball_color = ball.value_of_css_property("background-color")
            for basket in baskets[:]:  # Используем копию списка для безопасного удаления
                basket_color = basket.value_of_css_property("background-color")

                if basket_color == ball_color:
                    try:
                        ac.drag_and_drop(ball, basket).perform()
                        balls.remove(ball)  # Удаляем рамку из списка
                        break
                    except ElementClickInterceptedException:
                        print("Ошибка: не удалось выполнить перетаскивание. Повторная попытка.")
            else:
                print(f'Подходящий цвет для шарика {ball_color} не найден.')

    # Ждем появления сообщения о завершении задачи
    WebDriverWait(browser, poll_frequency=0.1, timeout=30).until(
        EC.text_to_be_present_in_element((By.CLASS_NAME, "message"), '')
    )
    print(browser.find_element(By.CLASS_NAME, "message").text)

