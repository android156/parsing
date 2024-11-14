from bs4 import BeautifulSoup

html_doc = """
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>Пример карточки товара</title>
</head>
<body>
    <div class="card">
        <img src="image.jpg" alt="Пример изображения товара">
        <h2 class="card-title"> iPhone 15 </h2>
        <p class="card-description">Аппаратной основой Apple iPhone 15 Pro Max стал 3-нанометровый чипсет A17 Pro с 6-ядерным GPU и поддержкой трассировки лучей.</p>
        <p class="card-price">999 999 руб.</p>
        <a href="https://example.com/product-link" class="card-link">Подробнее</a>
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

def main ():
    soup = BeautifulSoup(html_doc, 'lxml')
    p_description = soup.find('p', class_='card-description')
    print(p_description.text)

main()

# Поиск по ID:
#
# # Здесь 'tag' - это имя тега, а 'your_id' - значение атрибута id.
#
# soup.find('tag', id='your_id')
#
# Поиск по классу:
#
# # Заметьте, что используется class_ вместо class, так как class является зарезервированным словом в Python.
#
# soup.find('tag', class_='your_class')
#
# Поиск по пользовательскому атрибуту:
#
# # Здесь 'data-attribute' - это имя пользовательского атрибута, а 'value' - его значение.
#
# soup.find('tag', {'data-attribute': 'value'})
#
# Поиск по двойному пользовательскому атрибуту:
#
# # Здесь у тега одновременно должны быть два атрибута с заданными значениями.
#
# soup.find('tag', {'data-attribute1': 'value1', 'data-attribute2': 'value2'})
#
# Поиск по двойному классу:
#
# # Указываются оба класса, разделенные пробелом.
#
# soup.find('tag', class_='class1 class2')
#
# Поиск по динамическому классу:
#
# # Если класс формируется динамически и вы знаете только часть названия, можно использовать регулярные выражения:
#
# import re
# soup.find('tag', class_=re.compile('your_dynamic_part'))
#
# Поиск по динамическому пользовательскому атрибуту:
#
# # 'your_dynamic_part' - часть имени класса.
#
# soup.find('tag', {'data-attribute': re.compile('dynamic_part')})
#
# Поиск по тегу без атрибутов:
#
# # Просто укажите имя тега:
# # Это найдет первый тег с указанным именем без учета его атрибутов.
#
# soup.find('tag')
