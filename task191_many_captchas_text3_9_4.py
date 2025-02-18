import time

from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from twocaptcha import TwoCaptcha
from api_info import RU_CAPTCHA_API_KEY


def solve(browser, solver):
    question = browser.find_element(By.CSS_SELECTOR, ".chakra-form-control p").text.strip()
    if not question:
        return
    captcha_solve = solver.text(question)
    captcha_code = captcha_solve["code"]
    browser.find_element(By.CSS_SELECTOR, ".chakra-form-control .chakra-input").send_keys(captcha_code)
    browser.find_element(By.CSS_SELECTOR, ".chakra-form-control button").click()

    try:
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".main *")))
    except TimeoutException:
        captcha_id = captcha_solve["captchaId"]
        print(f"Bad code: {captcha_code}. Sending report for captcha id {captcha_id} ({question}).")
        solver.report(captcha_id, False)


def main():
    with webdriver.Chrome() as browser:
        solver = TwoCaptcha(RU_CAPTCHA_API_KEY)
        browser.get("https://captcha-parsinger.ru/text")
        WebDriverWait(browser, 60).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".main")))

        summ = 0

        while True:
            WebDriverWait(browser, 60).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".main")))
            while len(browser.find_elements(By.CSS_SELECTOR, ".chakra-form-control")) > 0:
                solve(browser, solver)
                time.sleep(1)

            numbers = browser.find_elements(By.CSS_SELECTOR, "ul li:first-child")
            summ += sum(int(e.text.strip("Артикул: ")) for e in numbers)

            if len(browser.find_elements(By.CSS_SELECTOR, ".pagination-next:not([disabled])")) > 0:
                browser.find_element(By.CSS_SELECTOR, ".pagination-next:not([disabled])").click()
                WebDriverWait(browser, 10).until(EC.url_changes(browser.current_url))
            else:
                break

        print(summ)


if __name__ == '__main__':
    start = time.time()
    main()
    print(f"Затрачено времени {time.time() - start} секунд")