import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from twocaptcha import TwoCaptcha
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from api_rucuptcha import API_ID

result = dict()
def main():
    url = 'https://captcha-parsinger.ru/text?page=1'
    url_base = 'https://captcha-parsinger.ru/text?page='
    options = webdriver.ChromeOptions()
    options.add_argument('--start-maximized')

    with webdriver.Chrome(options=options) as browser:
        browser.get(url)
        browser.implicitly_wait(2)

        # Находим все ссылки на страницы
        pages = [url_base + el.text for el in browser.find_elements(By.CSS_SELECTOR, ".pagination-page")]
        # print('pages =', pages)

        i = 0
        for page in pages:
            total = 0
            i += 1
            browser.get(page)
            browser.implicitly_wait(2)
            print(f'Обрабатываем страницу {i} из {len(pages)}...')
            # print('page =', page)
            if 'Подтвердите, что вы не робот' in browser.page_source:
                # time.sleep(5)
                # Находим элемент где располагается текст капчи, копируем его и отправляем на проверку
                question = browser.find_element(By.CSS_SELECTOR,
                                'div[class="chakra-form-control css-1sx6owr"]').find_element(
                                By.TAG_NAME, 'p')
                # условие ожидания, которое проверяет, является ли конкретный элемент видимым на веб-странице
                WebDriverWait(browser, 60).until(EC.visibility_of(question))
                question_text = question.text
                print('1) Получен вопрос от капчи: ', question_text)

                # вызываю объект solver
                print('2) Вопрос отправился на решение:')
                solver = TwoCaptcha(API_ID)
                print(f"Current money balance at RuCaptcha.com: {solver.balance()} rub")
                captcha_solve = solver.text(question_text)
                captcha_code = captcha_solve['code']
                captcha_id = captcha_solve['captchaId']
                print('3) От API пришёл ответ: ', captcha_solve)

                # Находим текстовое поле для вставки ответа на капчу и вставляем в него код captcha_solve
                # browser.find_element(By.ID, 'field-:r0:').send_keys(captcha_code)
                tag_input = browser.find_element(By.ID, 'field-:r0:')
                tag_input.send_keys(captcha_code)

                # Находим кнопку "Подтвердить" и кликаем по ней
                # browser.find_element(By.CSS_SELECTOR, 'button[class="chakra-button css-1wq39mj"]').click()
                confirm_button = browser.find_element(By.CSS_SELECTOR, 'button[class="chakra-button css-1wq39mj"]')
                confirm_button.click()
                time.sleep(1)

                try:
                    # ожидаем появления на странице всех товаров, которые находятся в области кода <div class="main">
                    block_elements = WebDriverWait(browser, 60).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".main *")))
                    if block_elements:
                        # Репортим о успешном решении капчи
                        solver.report(captcha_id, True)
                        print(f"Отправлен репорт о успешном разгадывании капчи с номером id: {captcha_id}")

                        # Решаем задачу
                        numbers = browser.find_elements(By.CSS_SELECTOR, "ul li:first-child")
                        total += sum(int(e.text.strip("Артикул:")) for e in numbers)
                        result[i] = total

                # если страница с товарами не загрузилась, то это означает, что капча не была разгадана
                # и тогда появится ошибка, чтобы этого не было - лучше обернуть весь блок с ожиданием в try - exept
                except TimeoutException:
                    print(f"Bad code: {captcha_code}. Sending report for captcha id {captcha_id} ({question_text}).")
                    solver.report(captcha_id, False)

            # если окна капчи нет на странице
            else:
                # ожидаем появления на странице всех товаров, которые находятся в области кода <div class="main">
                block_elements = WebDriverWait(browser, 60).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".main *")))
                if block_elements:
                    # Решаем задачу
                    numbers = browser.find_elements(By.CSS_SELECTOR, "ul li:first-child")
                    total += sum(int(e.text.strip("Артикул:")) for e in numbers)
                    result[i] = total

    return result

if __name__ == '__main__':
    start_time = time.perf_counter()
    dct = main()
    print(dct)
    total_sum = sum(map(lambda x: x[1], dct.items()))
    print('total_sum =', total_sum)
    end_time = time.perf_counter()
    print(f"Время выполнения программы: {end_time - start_time} cек.")

'''
Обрабатываем страницу 1 из 6...
Обрабатываем страницу 2 из 6...
Обрабатываем страницу 3 из 6...
1) Получен вопрос от капчи:  How many colours in the list blue, rainjacket, brown, pink, cat and snake?
2) Вопрос отправился на решение:
Current money balance at RuCaptcha.com: 99.384 rub
3) От API пришёл ответ:  {'captchaId': '78340315208', 'code': '3'}
Отправлен репорт о успешном разгадывании капчи с номером id: 78340315208
Обрабатываем страницу 4 из 6...
Обрабатываем страницу 5 из 6...
Обрабатываем страницу 6 из 6...
{1: 1466436218, 2: 1538477807, 3: 1251738721, 4: 1393846970, 5: 1320627657, 6: 1321573872}
total_sum = 8292701245
Время выполнения программы: 29.240441199974157 cек.
'''