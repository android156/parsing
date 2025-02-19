import requests
import os
from selenium import webdriver
from fake_useragent import UserAgent
from selenium.webdriver.common.by import By
from pydub import AudioSegment
import speech_recognition as sr
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import Keys


# ReCAPTCHA V2 обычно отображается как капча с изображением и кнопкой "Я не робот". Чтобы определить, что сайт
# использует ReCAPTCHA V2, вы можете:
#
#     Просмотреть исходный код страницы. Если вы видите тег <div class="g-recaptcha"> или ссылку на Google с текстом
#     "recaptcha", то скорее всего сайт использует ReCAPTCHA V2.
#
#     Воспользоваться дополнением браузера, которое позволяет найти различные скрипты и плагины на странице, например,
#     Wappalyzer.
#
# В этом примере, сайт использует ReCAPTCHA V2, так как в head подключен скрипт с url https://www.google.com/recaptcha
# /api.js, а в форме есть тег div с классом "g-recaptcha" и атрибутом data-sitekey, который содержит ключ сайта,
# необходимый для интеграции с ReCAPTCHA.
#
# Еще один способ определить, что сайт использует ReCAPTCHA V2, это найти скрипт с ссылкой
# https://www.google.com/recaptcha/api.js или https://www.google.com/recaptcha/api2/anchor?ar=1&k= на странице, это
# скрипты которые используются для работы ReCAPTCHA V2.

options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument(f"--user-agent={UserAgent().random}")


def write_audio(url, name_audio_file='audio.mp3'):
    response = requests.get(url)
    with open(f'{name_audio_file}', 'wb') as file:
        file.write(response.content)


def audio_to_text(mp3_file_name='audio.mp3', output_name='audio.wav'):
    audio = AudioSegment.from_mp3(mp3_file_name)
    audio.export(output_name, format="wav")
    recognizer = sr.Recognizer()
    with sr.AudioFile(output_name) as source:
        audio = recognizer.record(source)
    return recognizer.recognize_google(audio)


def is_recaptcha_present(browser):
    recaptcha_frames = browser.find_elements(By.CSS_SELECTOR, "iframe[title='reCAPTCHA']")
    return len(recaptcha_frames) > 0


def get_art_sum(browser, css_selector):
    items = browser.find_elements(By.CSS_SELECTOR, css_selector)
    return sum(int(item.text.split(': ')[-1].strip()) for item in items)


def main():
    with webdriver.Chrome(options=options) as browser:
        counter = 0
        for page in range(1, 7):
            browser.get(f'https://captcha-parsinger.ru/v2?page={page}')
            browser.implicitly_wait(10)

            if not is_recaptcha_present(browser):
                print("reCAPTCHA не обнаружена, продолжаем обработку страницы...")
                counter += get_art_sum(browser, "div.css-1ecvsm5 ul > li:first-child")
            else:
                print("Обнаружена reCAPTCHA, начинаем обработку...")

                WebDriverWait(browser, 20).until(
                    EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, "iframe[title='reCAPTCHA']"))
                )
                WebDriverWait(browser, 20).until(
                    EC.element_to_be_clickable((By.XPATH, '//*[@id="recaptcha-anchor"]/div[1]'))
                ).click()

                browser.switch_to.default_content()
                WebDriverWait(browser, 20).until(
                    EC.frame_to_be_available_and_switch_to_it(
                        (By.CSS_SELECTOR,
                         "iframe[title='текущую проверку reCAPTCHA можно пройти в течение ещё двух минут']"))
                )
                WebDriverWait(browser, 20).until(
                    EC.element_to_be_clickable((By.XPATH, '//*[@id="recaptcha-audio-button"]'))
                ).click()

                link_audio = browser.find_element(By.ID, "audio-source").get_attribute("src")
                write_audio(link_audio)

                try:
                    browser.find_element(By.CSS_SELECTOR, 'input[id="audio-response"]').send_keys(
                        audio_to_text().lower())
                    browser.find_element(By.ID, "audio-response").send_keys(Keys.ENTER)
                except Exception as e:
                    print(f"Ошибка при работе с reCAPTCHA: {e}")
                finally:
                    os.remove('audio.mp3')
                    os.remove('audio.wav')

                browser.switch_to.default_content()
                counter += get_art_sum(browser, "div.css-1ecvsm5 ul > li:first-child")

        print(f'Сумма артикулов: {counter}')


if __name__ == '__main__':
    main()