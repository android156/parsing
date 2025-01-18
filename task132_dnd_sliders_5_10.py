from selenium import webdriver
from selenium.common import ElementClickInterceptedException
from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options

options = Options()
options.headless = True
# Установите предпочтительное разрешение окна
options.add_argument("--window-size=1920,1080")# Можно поиграть с размерами и поставить их больше



url = "https://parsinger.ru/selenium/5.10/6/index.html"

with webdriver.Chrome(options=options) as browser:
    browser.get(url)

    # Ожидаем загрузки всех квадратов и рамок
    slider_containers = WebDriverWait(browser, poll_frequency=0.1, timeout=10).until(
        EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "div.slider-container")))
    print(len(slider_containers))
    print(slider_containers[0])
    ac = ActionChains(browser)

    # Двигаем сосочки

    for slider_container in slider_containers:
        slider_handler = slider_container.find_element(By.CSS_SELECTOR, 'input.volume-slider')
        target = int(slider_container.find_element(By.CSS_SELECTOR, 'span.target-value').text)
        current_value = int(slider_container.find_element(By.CSS_SELECTOR, 'span.current-value').text)

        while current_value != target:
            if current_value < target:
                slider_handler.send_keys(Keys.ARROW_RIGHT)
                current_value += 1
            else:
                # Уменьшаем значение
                slider_handler.send_keys(Keys.ARROW_LEFT)
                current_value -= 1

    # Ждем появления сообщения о завершении задачи
    WebDriverWait(browser, poll_frequency=0.1, timeout=30).until(
        EC.text_to_be_present_in_element((By.ID, "message"), '')
    )
    print(browser.find_element(By.ID, "message").text)

