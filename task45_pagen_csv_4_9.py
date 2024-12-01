from bs4 import BeautifulSoup
import requests
import csv

# Цикл по страницам пагинации, если не знаем и не нашли какая последняя

num_page = 1  # начнем с первой страницы

with open('res2.csv', 'w', encoding='utf-8-sig', newline='') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow(['Наименование',
                     'Артикул',
                     'Бренд',
                     'Модель',
                     'Тип',
                     'Технология экрана',
                     'Материал корпуса',
                     'Материал браслета',
                     'Размер',
                     'Сайт производителя',
                     'Наличие',
                     'Цена',
                     'Старая цена',
                     'Ссылка на карточку с товаром'])

# Создаем сессию
with requests.Session() as s:
    while True:
        url = f"https://parsinger.ru/html/index1_page_{num_page}.html"
        response = s.get(url)
        response.encoding = 'utf-8'


        # Если статус ответа 200, продолжаем парсинг
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'lxml')
            hrefs = [a.get('href') for a in soup.select('a.name_item')]

            for item_url in hrefs:
                full_url = f'https://parsinger.ru/html/{item_url}'
                print(full_url)

                response = s.get(full_url)
                response.encoding = 'utf-8'
                if response.status_code == 200:

                    soup = BeautifulSoup(response.text, 'lxml')
                    name = soup.select_one('p#p_header').text.strip()
                    article = soup.select_one('p.article').text.split(': ')[1].strip()
                    price = soup.select_one('span#price').text.strip()
                    old_price = soup.select_one('span#old_price').text.strip()
                    in_stock = soup.select_one('span#in_stock').text.split(': ')[1].strip()
                    li_list = soup.select('ul#description li')
                    print(li_list)
                    brand, model, _type, display, material_frame, material_bracer, size, site = [li.text.split(': ')[1].strip() for li in li_list]
                    print(name, article, brand, model, _type, display, material_frame, material_bracer, size, site, in_stock, price, old_price, full_url)
                    with open('res2.csv', 'a', encoding='utf-8-sig', newline='') as file:
                        writer = csv.writer(file, delimiter=';')
                        writer.writerow([name, article, brand, model, _type, display, material_frame, material_bracer, size, site, in_stock, price, old_price, full_url])
                else:
                    print(f'Ссылка {full_url} в карточке товара битая')


        else:
            # Если статус ответа не 200, завершаем цикл
            break
        num_page += 1


print('Готово!')