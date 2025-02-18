import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from twocaptcha import TwoCaptcha


# -----------------------3-----------------------------
def solver(question):
    solver = TwoCaptcha('e**************************c')
    print('Вопрос отправился на решение:', question)
    result = solver.text(question)
    print('От API пришёл ответ: ', result)
    return result['code']


# -----------------------3-----------------------------

with webdriver.Chrome() as browser:
    for x in range(1, 7):
        url = f'https://captcha-parsinger.ru/text?page={x}'
        browser.get(url)
        time.sleep(1)

        # -----------------------1-----------------------------
        if 'Подтвердите, что вы не робот' in browser.page_source:
            question_text = browser.find_element(By.CSS_SELECTOR,
            'div[class="chakra-form-control css-1sx6owr"]').find_element(By.TAG_NAME, 'p').text
            elem_button = browser.find_element(By.CSS_SELECTOR, 'button[class="chakra-button css-1wq39mj"]')
            input = browser.find_element(By.ID, 'field-:r0:').send_keys(solver(question_text))
            elem_button.click()
            time.sleep(2)
        # -----------------------1-----------------------------

        # -----------------------2-----------------------------
        while True:
            name_card = [x.text for x in browser.find_elements(By.CLASS_NAME, 'css-5ev4sb')]
            if len(name_card) > 0:
                print('Данные получены')
                print(url, name_card)
                break
            else:
                print('Решение не верное, ещё попытка')
                browser.find_element(By.ID, 'field-:r0:').send_keys(solver(question_text))
                elem_button.click()
                time.sleep(1)
                [name_card.append(x.text) for x in browser.find_elements(By.CLASS_NAME, 'css-5ev4sb')]
        # -----------------------2-----------------------------