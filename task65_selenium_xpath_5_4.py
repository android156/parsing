from selenium import webdriver
from selenium.webdriver.common.by import By

# URL веб-страницы для парсинга
url = 'http://parsinger.ru/selenium/3/3.html'

# Инициализируем драйвер Chrome
with webdriver.Chrome() as browser:
    # Открываем веб-страницу по заданному URL
    browser.get(url)

    # Используем метод .find_elements() для поиска всех элементов, соответствующих нашему XPath
    p_elements = browser.find_elements(By.XPATH, "//div[@class='text']/p[2]")

    # Проходимся по списку найденных элементов и выводим их текст
    for i, p_element in enumerate(p_elements):
        print(f"Текст второго p тега в {i + 1}-м div с классом 'text': {p_element.text}")

    # Ищем все div с классом 'text'
    divs = browser.find_elements(By.CLASS_NAME, 'text')

    print('*' * 100)

    # Проходимся по каждому div
    for i, div in enumerate(divs):
        # Получаем первый и третий теги <p> внутри каждого div
        first_p = div.find_element(By.XPATH, './p[1]')
        third_p = div.find_element(By.XPATH, './p[3]')

        # Выводим их текст
        print(f"Для div #{i + 1}, первый p: {first_p.text}, третий p: {third_p.text}")

    # Ищем родительский элемент
    parent_element = browser.find_element(By.ID, 'parent_id')
    # Ищем дочерний элемент внутри родительского
    child_element = parent_element.find_element(By.CLASS_NAME, 'child_class')

    # Или тот же самый поиск в одну строку
    element = browser.find_element(By.ID, 'parent_id').find_element(By.CLASS_NAME, 'child_class')

    # Ищем все блоки
    blocks = browser.find_elements(By.CLASS_NAME, 'block')
    # Проходим по каждому блоку и кликаем на кнопку внутри
    for block in blocks:
        button = block.find_element(By.CLASS_NAME, 'button')
        button.click()