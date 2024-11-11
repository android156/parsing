import re

from bs4 import BeautifulSoup

html_doc = """
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
</head>
<body>
    <div class="cards">
        <!-- Карточка товара 1 -->
        <div class="card">
            <img src="parsing.png" alt="WEB Парсинг на Python">
            <h2 class="card-title">WEB Парсинг на Python</h2>
            <p class="card-articul">Артикул: 104774</p>
            <p class="card-stock">Наличие: 5 шт.</p>
            <p class="card-price">3500 руб.</p>
            <a href="https://stepik.org/a/104774" class="card-button">Купить</a>
        </div>
        <!-- Карточка товара 2 -->
        <div class="card">
            <img src="async.png" alt="Асинхронный Python">
            <h2 class="card-title">Асинхронный Python</h2>
            <p class="card-articul">Артикул: 170777</p>
            <p class="card-stock">Наличие: 10 шт.</p>
            <p class="card-price">3500 руб.</p>
            <a href="https://stepik.org/a/170777" class="card-button">Купить</a>
        </div>
        <!-- Карточка товара 3 -->
        <div class="card">
            <img src="selenium.PNG" alt="Selenium Python">
            <h2 class="card-title">Selenium Python</h2>
            <p class="card-articul">Артикул: 119495</p>
            <p class="card-stock">Наличие: 5 шт.</p>
            <p class="card-price">1250 руб.</p>
            <a href="https://stepik.org/a/119495" class="card-button">Купить</a>
        </div>
    </div>
</body>
</html>
"""

# Заметьте, что используется class_ вместо class, так как class является зарезервированным словом в Python.

# soup.find('tag', class_='your_class')

# Здесь 'data-attribute' - это имя пользовательского атрибута, а 'value' - его значение.

# soup.find('tag', {'data-attribute': 'value'})

"""

    Обработать предоставленную HTML-структуру.
    Найти внутри неё тег <p> с классом card-description.
    Извлечь текстовое описание товара из найденного тега.

"""


# def main ():
#     soup = BeautifulSoup(html_doc, 'lxml')
#     p_description = soup.find('p', class_='card-description')
#     print(p_description.text)
#
# main()

def get_num_art(art):
    art_num = re.search(r'\d+', art)
    return int(art_num.group())


def main():
    # Инициализация объекта BeautifulSoup
    soup = BeautifulSoup(html_doc, 'lxml')
    # Поиск всех элементов с классом 'card-articul'

    articuls = soup.find_all('p', class_='card-articul')
    articuls = [get_num_art(art.text) for art in articuls]

    # Извлечение числовых значений артикулов и их суммирование
    sum_articuls = sum(articuls)

    print(f"Сумма артикулов: {sum_articuls}")  # Вывод результата


main()
