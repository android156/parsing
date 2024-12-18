import time

from selenium import webdriver
from selenium.common import NoAlertPresentException
from selenium.webdriver.common.by import By

with webdriver.Chrome() as driver:
    driver.get('https://parsinger.ru/selenium/5.8/5/index.html')

    # Переключаемся на iframe
    iframe_elements = driver.find_elements(By.TAG_NAME, 'iframe')
    codes = []
    for iframe in iframe_elements:
        driver.switch_to.frame(iframe)
        driver.find_element(By.TAG_NAME, 'button').click()
        codes.append(driver.find_element(By.CSS_SELECTOR, 'p#numberDisplay').text)
        driver.switch_to.default_content()

    print(codes)

    input_field = driver.find_element(By.CSS_SELECTOR, 'input#guessInput')
    input_button = driver.find_element(By.CSS_SELECTOR, 'button#checkBtn')
    for code in codes:
        input_field.clear()
        input_field.send_keys(code)
        input_button.click()
        time.sleep(0.1)
        try:
            alert = driver.switch_to.alert
            main_code = alert.text
            alert.accept()
            print('Кнопка нажата, Аллерт пойман')
            print(main_code)
        except NoAlertPresentException:
            print('Кнопка нажата, Аллерта нет', input_button.text)
            pass
    time.sleep(1)


# browser.execute_script("return arguments[0].scrollIntoView(true);", button)