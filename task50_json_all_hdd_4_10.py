from bs4 import BeautifulSoup
import requests
import csv
import json

# Цикл по страницам пагинации, если не знаем и не нашли какая последняя

num_page = 1  # начнем с первой страницы

test_json = {
    "Наименование": "Toshiba S300 Surveillance",
    "Бренд": "Toshiba",
    "Форм-фактор": "3.5",
    "Ёмкость": "4 Tb",
    "Объем буферной памяти": "128 Mb",
    "Цена": "10710 руб"
}

headers = ['Наименование', 'Бренд', 'Форм-фактор', 'Ёмкость', 'Объем буферной памяти', 'Цена']
result_json = []
# Создаем сессию
with requests.Session() as s:
    while True:
        url = f"https://parsinger.ru/html/index4_page_{num_page}.html"
        response = s.get(url)
        response.encoding = 'utf-8'
        # Если статус ответа 200, продолжаем парсинг
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'lxml')
            items_blocks = soup.select('div.img_box')

            for item in items_blocks:
                name = item.select_one('a.name_item').text.strip()
                price = item.select_one('p.price').text.strip()
                li_list = item.select('div.description li')
                brand, _type, _form, capacity = [li.text.split(': ')[1].strip() for li in li_list]
                values = [name, brand, _type, _form, capacity, price]

                result_json.append({header: value for header, value in zip(headers, values)})


        else:
            # Если статус ответа не 200, завершаем цикл
            break
        num_page += 1

with open('result.json', 'w', encoding='utf-8') as file:
    json.dump(result_json, file, indent=4, ensure_ascii=False)

# response = requests.get('http://parsinger.ru/html/watch/1/1_1.html')
# response.encoding = 'utf-8'
# soup = BeautifulSoup(response.text, 'lxml')
# description = soup.find('ul', id='description').find_all('li')
#
# for li in description:
#     print(li['id'])

#
# # 1 ------------------------------------------------------
# url = 'http://parsinger.ru/html/index3_page_1.html'
# response = requests.get(url=url)
# response.encoding = 'utf-8'
# soup = BeautifulSoup(response.text, 'lxml')
# # 1 ------------------------------------------------------
#
# # 2 ------------------------------------------------------
# name = [x.text.strip() for x in soup.find_all('a', class_='name_item')]
# description = [x.text.strip().split('\n') for x in soup.find_all('div', class_='description')]
# price = [x.text for x in soup.find_all('p', class_='price')]
# # 2 ------------------------------------------------------
#
# result_json = []
# # 3 ------------------------------------------------------
# for list_item, price_item, name in zip(description, price, name):
#     result_json.append({
#         'name': name,
#         'brand': [x.split(':')[1] for x in list_item][0],
#         'type': [x.split(':')[1] for x in list_item][1],
#         'connect': [x.split(':')[1] for x in list_item][2],
#         'game': [x.split(':')[1] for x in list_item][3],
#         'price': price_item
#
#     })
#
# # 3 ------------------------------------------------------
#
# # 4 ------------------------------------------------------
# with open('res.json', 'w', encoding='utf-8') as file:
#     json.dump(result_json, file, indent=4, ensure_ascii=False)
# # 4 ------------------------------------------------------
#
# В этом коде активно применялись list comprehension для извлечения необходимых данных и формирования списка словарей.
#
#     В блоке №1 нет ничего нового для вас;
#     В блоке №2 мы извлекаем информацию с каждой карточки на сайте тренажёре, извлекаем наименование товара, его описание и стоимость. Если мы посмотрим на элементы страницы HTML, мы увидим,  что description  извлекается методом find_all() и получается список списков, который необходимо записать в наш список словарей;
#     В этом блоке мы инициируем цикл, в котором проходимся по трём основным спискам, мы создали их в блоке 2, и на каждой итерации записываем значение в соответствующий ключ нашего словаря.
#
# В результате выполнения этого кода мы получаем файл res.json в каталоге с нашим проектом
