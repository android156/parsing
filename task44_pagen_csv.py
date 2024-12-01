from bs4 import BeautifulSoup
import requests
import csv

# Цикл по страницам пагинации, если не знаем и не нашли какая последняя

num_page = 1  # начнем с первой страницы

with open('res.csv', 'w', encoding='utf-8-sig', newline='') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow([
        'Наименование', 'Бренд', 'Форм-фактор', 'Ёмкость', 'Объем буферной памяти', 'Цена'])

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
                print(name, brand, _type, _form, capacity, price)
                with open('res.csv', 'a', encoding='utf-8-sig', newline='') as file:
                    writer = csv.writer(file, delimiter=';')
                    writer.writerow([name, brand, _type, _form, capacity, price])


        else:
            # Если статус ответа не 200, завершаем цикл
            break
        num_page += 1


print('Готово!')