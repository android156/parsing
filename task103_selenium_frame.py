from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as driver:
    driver.get('https://parsinger.ru/selenium/5.8/4/index.html')

    # Переключаемся на iframe
    iframe_element = driver.find_element(By.TAG_NAME, 'iframe')
    driver.switch_to.frame(iframe_element)

    # Извлекаем HTML содержимое из iframe
    iframe_content = driver.page_source
    # Выход из фрейма: Чтобы выйти из iFrame или frameset, вернитесь к содержимому по умолчанию.
    driver.switch_to.default_content()
    print(iframe_content)



# Используя WebElement: Это наиболее гибкий вариант. Вы можете найти фрейм с помощью вашего предпочтительного
# iframe = driver.find_element(By.CSS_SELECTOR, "#modal > iframe")
# driver.switch_to.frame(iframe)
# driver.find_element(By.TAG_NAME, 'button').click()

# Используя имя или ID: Если у вашего фрейма или iFrame есть атрибуты id или name, вы можете использовать их.
# driver.switch_to.frame('buttonframe')
# driver.find_element(By.TAG_NAME, 'button').click()

# Используя индекс: Также можно использовать индекс фрейма.
#
# driver.switch_to.frame(1)
#
#
# Выход из фрейма: Чтобы выйти из iFrame или frameset, вернитесь к содержимому по умолчанию.
#
# driver.switch_to.default_content()