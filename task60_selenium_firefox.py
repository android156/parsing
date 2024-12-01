import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options

# Укажите путь к расширению - .xpi файлу
extension_path = "{b018dad2-41b4-47bb-997b-1726c72b8883}.xpi"

options = Options()
# options.add_argument("--start-maximized")  # Запуск браузера в полноэкранном режиме
options.add_argument("--headless") # Включение скрытого режима
options.set_preference("extensions.autoDisableScopes", 0)  # Разрешение установки расширений
options.add_argument('--disable-gpu')

with webdriver.Firefox(
        service=FirefoxService(GeckoDriverManager().install()), options=options) as driver:

    # для установки расширения
    driver.install_addon(extension_path, temporary=True)
    # driver.get("https://stepik.org/course/104774")
    driver.get('https://yandex.ru/')
    # input("Press Enter to quit...")
    # time.sleep(5)
    a = driver.find_element(By.TAG_NAME, 'a')

    # Выводим атрибут 'href' найденного элемента (URL ссылки)
    print(a.get_attribute('href'))
