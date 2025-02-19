import time
from seleniumwire import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

def main():
    # Инициализация браузера с seleniumwire
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    with webdriver.Chrome(options=options) as browser:
        browser.get('https://captcha-parsinger.ru/v2?page=3')

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
        # time.sleep(200)
        WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.ID, 'recaptcha-audio-button'))
        ).click()
        # #recaptcha-audio-button

        # Клик по кнопке "Прослушать"
        WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.ID, '\:2'))
        ).click()

        # #\:2

        # Перехват запроса на аудиофайл через seleniumwire
        audio_src = None
        for request in browser.requests:
            if "payload" in request.path and request.response and (
                    request.response.headers.get('Content-Type') == 'audio/mp3'):
                audio_src = request.url  # Получаем полный URL аудиофайла
                break

        if audio_src:
            print(f"[INFO] Audio src intercepted: {audio_src}")
        else:
            print("[ERROR] Audio src not found in intercepted requests")

        time.sleep(5)

if __name__ == '__main__':
    main()