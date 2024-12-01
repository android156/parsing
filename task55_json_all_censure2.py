import requests
from bs4 import BeautifulSoup
import json
from typing import Optional, Dict

# Определяем заголовки для HTTP-запроса
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, как Gecko) Chrome/89.0.4389.82 Safari/537.36'
}


def get_soup(url: str) -> Optional[BeautifulSoup]:
    """
    Выполняет GET-запрос к указанному URL и возвращает объект BeautifulSoup
    для парсинга HTML, или None, если запрос не удался.
    Аргументы: url (str): URL-адрес для парсинга.
    """
    response = requests.get(url, headers=headers)
    response.encoding = 'utf-8'
    return BeautifulSoup(response.text, 'html.parser') if response.status_code == 200 else None


def get_value(selector: str) -> str:
    """
    Извлекает текстовое значение из HTML-элемента, найденного по CSS-селектору.
    Если элемент содержит двоеточие, возвращается часть после двоеточия.
    Аргументы: selector (str): CSS-селектор для целевого HTML-элемента.
    """
    element = soup.select_one(selector)
    return (element.text.split(': ')[-1].strip() if ':' in element.text else element.text) if element else ""


# Парсим данные и сохраняем их в список словарей
data = [
    {
        'categories': menu_name,  # Название категории
        'name': get_value('#p_header'),  # Название продукта
        'article': get_value('.article'),  # Артикул продукта
        'description': {''.join(list(tag.attrs.values())): tag.text.split(': ')[-1].strip() for tag in
                        soup.select('li')},  # Описание продукта
        'count': get_value('#in_stock'),  # Количество на складе
        'price': get_value('#price'),  # Текущая цена
        'old_price': get_value('#old_price'),  # Цена до скидки
        'link': url  # URL-адрес страницы продукта
    }
    for index, menu_name in enumerate(['watch', 'mobile', 'mouse', 'hdd', 'headphones'], 1)  # Перебор категорий
    for page in range(1, 33)  # Проход по 32 страницам на каждую категорию
    if (soup := get_soup(url := f'https://parsinger.ru/html/{menu_name}/{index}/{index}_{page}.html'))
    # Запрос и парсинг страницы
]

# Сохранение собранных данных в файл JSON
with open('res2.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, indent=4, ensure_ascii=False)

print('Данные успешно загружены')
