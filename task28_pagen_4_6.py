from bs4 import BeautifulSoup
import requests
import pyperclip


# Цикл по страницам пагинации, если не знаем и не нашли какая последняя

num_page = 1  # начнем с первой страницы
base_url = f"https://parsinger.ru/html/index3_page_{num_page}.html"
mouse_lists = []
# Создаем сессию
with requests.Session() as s:

    while True:
        url = f"https://parsinger.ru/html/index3_page_{num_page}.html"
        response = s.get(url)
        response.encoding = 'utf-8'
        # Если статус ответа 200, продолжаем парсинг
        if response.status_code == 200:
            # Здесь ваш код для парсинга содержимого страницы
            soup = BeautifulSoup(response.text, 'lxml')
            items_blocks = soup.select('div.img_box')
            name_list = []
            for item in items_blocks:
                it_name = item.select_one('a.name_item').text
                it_type = item.select_one('div.description li').next_sibling.next_sibling.text.strip()
                
                if 'мышь' in it_type.lower():
                    name_list.append(it_name)
            if len(name_list) > 0:
                mouse_lists.append(name_list)
        else:
            # Если статус ответа не 200, завершаем цикл
            break
        num_page += 1
print(mouse_lists)

# Сохраняем результат в буфер обмена
pyperclip.copy(mouse_lists)


