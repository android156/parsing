
# Подгружаем необходимые пакеты
from bs4 import BeautifulSoup
import lxml
import requests
from fake_useragent import UserAgent
import csv

# Инициируем сессию и создаем экземляр класса UserAgent для фейковых заголовков
ses = requests.session()
ua = UserAgent()


def souped(session, relative_url):
    '''
    скрэпит и парсит сайт через requests и bs4, используя парсер lxml и рандомный заголовок 'user-agent'
    '''
    fake_ua = {'user-agent': ua.random}
    html = session.get(f'https://parsinger.ru/html/{relative_url}', headers=fake_ua)
    html.encoding = 'utf-8-sgi'
    return BeautifulSoup(html.text, 'lxml')

# скрэпим все относительные ссылки на категории товаров
soup0 = souped(ses, 'index1_page_1.html')
cat_pages = soup0.select('div.nav_menu a')

# Заголовки будущей таблицы
headers = ['Наименование', 'Артикул', 'Бренд', 'Модель', 'Наличие', 'Цена', 'Старая цена', 'Ссылка на карточку с товаром']

# Открываем контекстный менеджер файла вне цикла, чтобы не открывать его 1000 раз
with open('result1.csv', 'w', encoding='utf-8-sig') as f:

    # Инициализируем экземляр класс csv и записываем первой строкой заголовки
    writer = csv.writer(f, delimiter=';')
    writer.writerow(headers)

    # Проходимся циклом по всем категориям, собирая все относительные ссылки на страницы внутри категории
    for cat_page in cat_pages:
        # Проверяем, доступна ли категория
        try:
            soup1 = souped(ses, cat_page['href'])
            pages = soup1.select(':nth-child(1 of div.pagen) a')
        except requests.ConnectionError as e:
            print(f"Нет доступа к {cat_page.text}")
            continue

        # Проходимся циклом по страницам категории и парсим ее
        for page in pages:
            # Проверяем, доступна ли страница внутри категории
            try:
                soup = souped(ses, page['href'])
            except requests.ConnectionError as e:
                print(f'нет доступа к {page.text} странице раздела {cat_page.text}')
                continue

            # Проходимся циклом по именам товаров, и цепляем оттуда ссылку на карточку
            for item_name in soup.find_all(class_='name_item'):
                item_page = souped(ses, item_name['href'])

                # Собираем все необходимые данные из карточки
                name = item_page.find(id='p_header').text
                article = item_page.find(class_='article').text.split()[-1]
                descr = map(lambda x: x.text.split(': ')[1], item_page.select('ul#description li:nth-child(-n + 2)'))
                stock = item_page.find(id='in_stock').text.split()[-1]
                price = item_page.find(id='price').text
                old_price = item_page.find(id='old_price').text

                # Вставляем строку данных в наш файл через writer'а
                writer.writerow \
                    ([name, article, *descr, stock, price, old_price, 'https://parsinger.ru/html/' + item_name['href']])


