import time
from selenium import webdriver
from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from twocaptcha import TwoCaptcha
import itertools
import pydub
import requests
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import seleniumwire.undetected_chromedriver as uc
from seleniumwire import webdriver as wire_webdriver
from fake_useragent import UserAgent
import speech_recognition as sr
from selenium.webdriver import Keys

name_audio_file = 'audio_file.mp3'


def write_audio(url):
    response = requests.get(url)
    with open(f'{name_audio_file}', 'wb') as file:
        file.write(response.content)


def audio_to_text():
    path_to_mp3 = name_audio_file
    path_to_wav = 'audio_file_wav.wav'
    sound = pydub.AudioSegment.from_file(path_to_mp3, 'mp3')
    sound.export(path_to_wav, format="wav")
    sample_audio = sr.AudioFile(path_to_wav)
    r = sr.Recognizer()
    with sample_audio as source:
        audio = r.record(source)
    key = r.recognize_google(audio)
    return key


class ProxyRotator:
    def __init__(self, proxies):
        # создает итератор, который будет перебирать прокси-сервера в цикле
        self.proxies = itertools.cycle(proxies)
        # хранит текущий используемый прокси-сервер
        self.current_proxy = None
        # счетчик запросов, для определения когда нужно сменить прокси-сервер
        self.request_counter = 0

    def change_proxy(self):
        # меняет текущий используемый прокси-сервер на следующий в списке
        self.current_proxy = next(self.proxies)
        # сбрасывает счетчик запросов
        self.request_counter = 0
        return self.current_proxy

    def get_proxy(self):
        # проверяет нужно ли сменить пр
        # проверяет нужно ли сменить прокси-сервер
        # где 2, означает, что прокси будут изменены после каждого второго запроса
        if self.request_counter % 2 == 0:
            self.change_proxy()
        # увеличивает счетчик запросов
        self.request_counter += 1
        return self.current_proxy


# 5.101.91.200:8000:TdWubd:s914RN
# 5.8.60.177:8000:TdWubd:s914RN
proxies = [
    {'http': "socks5://TdWubd:s914RN@5.101.91.200:8000", 'https': "socks5://TdWubd:s914RN@5.101.91.200:8000"},
    {'http': "socks5://TdWubd:s914RN@5.8.60.177:8000", 'https': "socks5://TdWubd:s914RN@5.8.60.177:8000"},
    # {'http': "socks5://4bL6Jn:SEKwVS@196.18.167.105:8000", 'https': "socks5://4bL6Jn:SEKwVS@196.18.167.105:8000"},
    # {'http': "socks5://wRKZPG:snFyfD@91.229.113.96:8000", 'https': "socks5://wRKZPG:snFyfD@91.229.113.96:8000"}
]

proxy_rotator = ProxyRotator(proxies)

main_url = 'https://captcha-parsinger.ru/v2'


def check_captcha(browser):
    time.sleep(0.5)
    try:
        browser.find_element(By.CSS_SELECTOR, "iframe[title='reCAPTCHA']")
    except NoSuchElementException:
        return False
    return True


def access_denied(next_button: WebElement):
    bool_dict = {"true": True, "false": False}
    is_next_button_disabled = bool_dict[next_button.get_attribute('aria-disabled')]
    return is_next_button_disabled


def solve_recaptcha(browser):
    # Ожидание появления iframe с чекбоксом reCAPTCHA и переключение в него
    WebDriverWait(browser, 10).until(
        EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, "iframe[title='reCAPTCHA']"))
    )
    # Клик по чекбоксу reCAPTCHA
    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.ID, 'recaptcha-anchor'))
    ).click()

    # Возвращаемся в основной контекст страницы
    browser.switch_to.default_content()

    # Ожидание появления iframe с набором картинок и переключение в него
    WebDriverWait(browser, 10).until(
        EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, "iframe[title*='текущую проверку reCAPTCHA']"))
    )

    # Клик по кнопке "Аудио"

    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.ID, 'recaptcha-audio-button'))
    ).click()
    # #recaptcha-audio-button

    # Клик по кнопке "Прослушать"
    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.ID, '\:2'))
    ).click()
    time.sleep(2)
    # time.sleep(200)

    # Перехват запроса на аудиофайл через seleniumwire
    audio_src = None
    for request in browser.requests:
        if "payload" in request.path and request.response and (
                request.response.headers.get('Content-Type') == 'audio/mp3'):
            audio_src = request.url  # Получаем полный URL аудиофайла
            break

    if audio_src:
        print(f"[INFO] Audio src intercepted: {audio_src}")
        write_audio(audio_src)
        time.sleep(2)
        browser.find_element(By.CSS_SELECTOR, 'input[id="audio-response"]').send_keys(audio_to_text().lower())
        browser.find_element(By.ID, "audio-response").send_keys(Keys.ENTER)
        time.sleep(2)
        # Переключаемся обратно на основной контент страницы
        browser.switch_to.default_content()

    else:
        print("[ERROR] Audio src not found in intercepted requests")

    time.sleep(1)



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
    if check_captcha(browser):
        print('Тут есть капча.')
        print('Разгадка капчи, попытка: 1')
        solve_recaptcha(browser)
        attempts = 1
        while True:
            success, result = get_elements_with_selector(selector, single_mode)
            if success:
                print('Капча разгадана!')
                print((len(result), result) if isinstance(result, list) else result.tag_name)
                break
            else:
                if attempts > 3:
                    raise Exception('Капчу разгадать не удалось')
                print("Капча решена неверно, повторяем попытку")
                attempts += 1
                print('Разгадка капчи, попытка: ', attempts)
                solve_recaptcha(browser)

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
stop_flag = False
while True:
    if stop_flag:
        break
    proxy = proxy_rotator.get_proxy()
    print(f'using proxy: {proxy}')
    prx = {}
    prx.update({'proxy': proxy})
    ua = UserAgent()
    options = uc.ChromeOptions()
    options.add_argument(f"--user-agent={ua}")
    options.add_argument("--ignore-certificate-errors")
    options.add_argument("--unsafely-treat-insecure-origin-as-secure=https://captcha-parsinger.ru")
    with uc.Chrome(main_version=109, chrome_options=options, seleniumwire_options=prx) as browser:
        browser.get(main_url)
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
                stop_flag = True
                break

print(len(total_art), total_art)
print(sum(total_art))
