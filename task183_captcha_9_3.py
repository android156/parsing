import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from twocaptcha import TwoCaptcha

#Функция принимает путь до изображения и отправляет изображение в API rucaptcha, после получения разгаданной капчи, функция возвращает код который находился на капче

def sender_solve(path):
    solver = TwoCaptcha('57d1ab924bbe71592a3ab2b8a46d34d4')
    print('2) Изображение отправлено для разгадывания:')
    result = solver.normal(path)
    print('3) От API пришёл ответ: ', result)
    return result['code']


with webdriver.Chrome() as browser:
    browser.get('https://captcha-parsinger.ru/?page=3')
    #используем неявное ожидание для полной загрузки страницы и появления всех элементов.
    browser.implicitly_wait(10)
    #Это условие if проверит в исходном коде ключевую фразу для определения на странице капчи.
    if 'Подтвердите, что вы не робот' in browser.page_source:
        #Находим элемент где располагается изображение капчи и делаем его скриншот, .screenshot('img.png') сохраняет скриншот в папке с проектом,
        #но можно написать и полный путь, тогда его необходимо будет передать в solver()
        browser.find_element(By.CSS_SELECTOR, 'div[class="chakra-form-control css-1sx6owr"]').find_element(By.TAG_NAME,'img').screenshot('captchas/img.png')
        print('1) Скриншот области успешно сделан')
        #Находим текстовое поле и вставляем код который возвращает функция solver(),
        browser.find_element(By.ID, 'field-:r0:').send_keys(sender_solve('captchas/img.png'))
        #Находим кнопку "Подтвердить" и кликаем по ней.
        browser.find_element(By.CSS_SELECTOR, 'button[class="chakra-button css-1wq39mj"]').click()

    #Собираем список наименований всех товарных позиций на странице
    name_card = [x.text for x in browser.find_elements(By.CLASS_NAME, 'css-5ev4sb')]
    print('4)',name_card)