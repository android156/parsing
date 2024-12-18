import time
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    time.sleep(1)
    browser.execute_script('window.open("http://parsinger.ru/blank/0/1.html", "_blank1");')
    browser.execute_script('window.open("http://parsinger.ru/blank/0/2.html", "_blank2");')
    browser.execute_script('window.open("http://parsinger.ru/blank/0/3.html", "_blank3");')
    browser.execute_script('window.open("http://parsinger.ru/blank/0/4.html", "_blank4");')
    browser.execute_script('window.open("http://parsinger.ru/blank/0/5.html", "_blank5");')
    browser.execute_script('window.open("http://parsinger.ru/blank/0/6.html", "_blank6");')
    browser.execute_script('window.open("http://parsinger.ru/blank/2/1.html", "_blank7");')
    browser.execute_script('window.open("http://parsinger.ru/blank/2/2.html", "_blank8");')
    browser.execute_script('window.open("http://parsinger.ru/blank/2/3.html", "_blank9");')
    browser.execute_script('window.open("http://parsinger.ru/blank/2/4.html", "_blank10");')
    print(browser.window_handles)
    for page in browser.window_handles:
        browser.switch_to.window(page)
        for y in browser.find_elements(By.CLASS_NAME, 'check'):
            y.click()
    for page in browser.window_handles:
        browser.switch_to.window(page)
        time.sleep(1)
        print(browser.execute_script("return document.title;"), page)
    time.sleep(10)

    #
    # import time
    #
    # from selenium.webdriver import Chrome
    #
    #
    # pages = ["http://parsinger.ru/blank/0/1.html",
    #          "http://parsinger.ru/blank/0/2.html",
    #          "http://parsinger.ru/blank/0/3.html",
    #          "http://parsinger.ru/blank/0/4.html",
    #          "http://parsinger.ru/blank/0/5.html",
    #          "http://parsinger.ru/blank/0/6.html"
    #          ]
    #
    # with Chrome() as browser:
    #     for page in pages:
    #         browser.switch_to.new_window("tab")
    #         browser.get(page)
    #     time.sleep(2)
    #
    #     for page in browser.window_handles:
    #         browser.switch_to.window(page)
    #         time.sleep(1)
    #
    #         # Получаем title вкладки
    #         title = browser.execute_script("return document.title;")
    #         print(title, page)