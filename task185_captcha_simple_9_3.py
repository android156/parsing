import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from twocaptcha import TwoCaptcha

solver = TwoCaptcha('57d1ab924bbe71592a3ab2b8a46d34d4')
# Создаём словарь для того чтобы положить в него результат ответа на API {'captchaId': '72447681441', 'code': 'gbkd'}
dict_resut = {}
img_name = 'captchas/img3.png'
main_url = 'https://captcha-parsinger.ru/'


def sender_solve(path=img_name):
    print('2) Изображение отправлено для разгадывания:')
    result = solver.normal(path)
    print('3) От API пришёл ответ: ', result)
    # API вернёт словарь {'captchaId': '72447681441', 'code': 'gbkd'}
    # Обновляем словарь для дальнейшего извлечения ID капчи и отправки репорта
    dict_resut.update(result)
    return result['code']


main_url = 'https://captcha-parsinger.ru/'


def check_captcha(website_html):
    if 'Подтвердите, что вы не робот' in website_html:
        return True
    return False


def access_denied(next_button: WebElement):
    bool_dict = {"true": True, "false": False}
    is_next_button_disabled = bool_dict[next_button.get_attribute('aria-disabled')]
    return is_next_button_disabled


def solve_captcha(browser):
    browser.find_element(
        By.CSS_SELECTOR, 'div[class="chakra-form-control css-1sx6owr"]'
    ).find_element(By.TAG_NAME, 'img').screenshot(img_name)
    print('1) Скриншот области успешно сделан')
    browser.find_element(By.ID, 'field-:r0:').send_keys(sender_solve())
    browser.find_element(By.CSS_SELECTOR, 'button[class="chakra-button css-1wq39mj"]').click()

def get_result(browser, selector, single_mode=True):
    def get_elements_with_selector(selector, single_mode):
        res = False
        if single_mode:
            result = browser.find_element(By.CSS_SELECTOR, selector)
            if result:
                res = True
        else:
            result = [int((x.text).split(': ')[1]) for x in browser.find_elements(By.CSS_SELECTOR, selector)]
            if len(result) > 0:
                res = True
        return res, result

    print(f'Исследуем страницу: {browser.current_url}, селектор: {selector}')
    if check_captcha(browser.page_source):
        print('Тут есть капча.')
        print('Разгадка капчи, попытка: 1')
        solve_captcha(browser)
        attempts = 1
        while True:
            success, result = get_elements_with_selector(selector, single_mode)
            if success:
                # Репортим об успешном решении
                solver.report(dict_resut['captchaId'], True)
                print(f"Отправлен репорт об успешном разгадывании. id:{dict_resut['captchaId']}")
                print((len(result), result) if isinstance(result, list) else result.tag_name)
                break
            else:
                if attempts > 3:
                    raise Exception('Капчу разгадать не удалось')
                print("Капча решена неверно, повторяем попытку")
                attempts += 1
                # Репортим о неудачной попытке разагадать капчу
                print(f"Отправлен репорт о неуспешной попытке. id:{dict_resut['captchaId']}")
                solver.report(dict_resut['captchaId'], False)
                print('Разгадка капчи, попытка: ', attempts)
                solve_captcha(browser)

    else:
        success, result = get_elements_with_selector(selector, single_mode)
        if success:
            print('Тут нет капчи.')
            print((len(result), result) if isinstance(result, list) else result.tag_name)
        else:
            print('Не нашли ничего по селектору: ', selector)
            time.sleep(2)

    return result

total_art = []
with webdriver.Chrome() as browser:
    browser.get(main_url)
    browser.implicitly_wait(10)
    page_counter = 0
    while True:
        page_counter += 1
        print('Страница: ', page_counter)
        total_art.extend(get_result(browser, '.css-1ecvsm5 > ul > li:first-child', single_mode=False))
        next_button = get_result(browser, 'button[aria-label="Next page"]', )
        if not access_denied(next_button):
            next_button.click()
            time.sleep(2)
        else:
            break

print(len(total_art), total_art)
print(sum(total_art))


