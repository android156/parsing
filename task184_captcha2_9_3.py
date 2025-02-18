import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from twocaptcha import TwoCaptcha


solver = TwoCaptcha('57d1ab924bbe71592a3ab2b8a46d34d4')
#Создаём словарь для того чтобы положить в него результат ответа на API {'captchaId': '72447681441', 'code': 'gbkd'}
dict_resut = {}
img_name = 'captchas/img2.png'

def sender_solve(path=img_name):
    print('2) Изображение отправлено для разгадывания:')
    result = solver.normal(path)
    print('3) От API пришёл ответ: ', result)
    #API вернёт словарь {'captchaId': '72447681441', 'code': 'gbkd'}
    #Обновляем словарь для дальнейшего извлечения ID капчи и отправки репорта
    dict_resut.update(result)
    return result['code']


with webdriver.Chrome() as browser:
    browser.get('https://captcha-parsinger.ru/?page=3')
    browser.implicitly_wait(10)
    if 'Подтвердите, что вы не робот' in browser.page_source:
        browser.find_element(By.CSS_SELECTOR, 'div[class="chakra-form-control css-1sx6owr"]').find_element(By.TAG_NAME,'img').screenshot(img_name)
        print('1) Скриншот области успешно сделан')
        browser.find_element(By.ID, 'field-:r0:').send_keys(sender_solve())
        browser.find_element(By.CSS_SELECTOR, 'button[class="chakra-button css-1wq39mj"]').click()
        #Запускаем бесконечный цикл на случай, если неудачных попыток будет несколько.
        while True:
            #Пытаемся спарсить список товаров
            name_card = [x.text for x in browser.find_elements(By.CLASS_NAME, 'css-5ev4sb')]
            #Если спарсить не получилось, и список name_card не содержит элементов, то переходим в блок else
            if len(name_card) > 0:
                #Репортим о успешном решении
                solver.report(dict_resut['captchaId'], True)
                print(f"Отправлен репорт об успешном разгадывании. id:{dict_resut['captchaId']}")
                print('4)',name_card)
                #После успешного получения данных, прерываем цикл
                break
            else:
                print("Капча решена неверно, повторяем попытку")
                #Репортим о неудачной попытке разагадать капчу
                print(f"Отправлен репорт о неуспешной попытке. id:{dict_resut['captchaId']}")
                solver.report(dict_resut['captchaId'], False)
                #Делаем новый скриншот, т.к. после неуспешной попытки капча обновилась
                print('Повторный скриншот области')
                browser.find_element(By.CSS_SELECTOR, 'div[class="chakra-form-control css-1sx6owr"]').find_element(
                    By.TAG_NAME, 'img').screenshot('captchas/img2.png')
                #Отправляем скриншот повторно
                browser.find_element(By.ID, 'field-:r0:').send_keys(sender_solve())
                #Кликаем кнопку повторно
                browser.find_element(By.CSS_SELECTOR, 'button[class="chakra-button css-1wq39mj"]').click()
                #Пытаемся наполнить список name_card найденными элементами
                [name_card.append(x.text) for x in browser.find_elements(By.CLASS_NAME, 'css-5ev4sb')]