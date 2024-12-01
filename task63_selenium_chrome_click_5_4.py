import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get('http://parsinger.ru/html/watch/1/1_1.html')
button = browser.find_element(By.ID, "sale_button").click()

# .click() для симуляции клика мышью.
# browser.find_element(By.ID, "some_button_id").click()
#
# .send_keys() для ввода текста (полезно для текстовых полей).
# browser.find_element(By.NAME, "some_textbox_name").send_keys("Hello, World!")
#
# .get_attribute('some_attribute') для получения атрибутов, например, href у ссылок.
# browser.find_element(By.TAG_NAME, "a").get_attribute("href")
#
# .text для получения видимого текста элемента.
# browser.find_element(By.CLASS_NAME, "some_class_name").text

time.sleep(10)

# By.ID – Поиск элемента по уникальному идентификатору (id). Этот метод очень быстрый и надежный, но требует, чтобы у элемента был атрибут id.
# element = driver.find_element(By.ID, "some_id")
#
# By.CSS_SELECTOR – Поиск элемента или элементов, используя селекторы CSS. Это гибкий и мощный метод, который может выразить сложные критерии поиска.
# elements = driver.find_elements(By.CSS_SELECTOR, ".some_class")
#
# By.XPATH – Поиск элемента с помощью языка XPath. XPath позволяет создать более сложные запросы, но он менее читаемый и, возможно, будет работать медленнее, чем другие методы.
# element = driver.find_element(By.XPATH, "//div[@attribute='value']")
#
# By.NAME – Поиск элемента по атрибуту name. Этот метод хорошо подходит для форм.
# element = driver.find_element(By.NAME, "username")
#
#By.TAG_NAME – Поиск элемента по названию HTML-тега. Этот метод полезен, если нужно выбрать, например, все изображения на странице.
# images = driver.find_elements(By.TAG_NAME, "img")
#
# By.CLASS_NAME – Поиск элемента или элементов по классу. Этот метод полезен, если у элементов есть общий класс.
# buttons = driver.find_elements(By.CLASS_NAME, "btn")
#
# By.LINK_TEXT – Поиск элемента по точному тексту ссылки. Очень удобно, если текст уникален.
# element = driver.find_element(By.LINK_TEXT, "Continue")
#
# By.PARTIAL_LINK_TEXT – Поиск элемента по частичному тексту ссылки. Удобно, когда точный текст ссылки неизвестен или динамичен.
# element = driver.find_element(By.PARTIAL_LINK_TEXT, "Cont")