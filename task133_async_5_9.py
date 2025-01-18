import asyncio
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait


async def wait_and_click_checkbox(driver, checkbox, check_button):
    # Асинхронное ожидание элемента (обернуто в asyncio.to_thread)
    await asyncio.to_thread(
        WebDriverWait(driver, 10).until,
        ec.element_to_be_selected(checkbox))
    # Синхронный клик по кнопке
    check_button.click()


async def main():
    tasks = []
    with webdriver.Chrome() as browser:
        browser.get('https://parsinger.ru/selenium/5.9/7/index.html')
        containers = browser.find_elements(By.CLASS_NAME, 'container')
        for container in containers:
            check_button = container.find_element(By.TAG_NAME, 'button')
            checkbox = container.find_element(By.TAG_NAME, 'input')
            # Создаем асинхронную задачу
            task = asyncio.create_task(wait_and_click_checkbox(browser, checkbox, check_button))
            tasks.append(task)
        await asyncio.gather(*tasks)


start = time.time()
asyncio.run(main())
print(f'Время выполнения: {time.time() - start}')
