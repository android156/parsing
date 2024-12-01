import csv
import aiohttp
import asyncio
from aiofiles import open as aio_open
from bs4 import BeautifulSoup

url = 'https://parsinger.ru/html/index1_page_1.html'
schema = 'http://parsinger.ru/html/'

async def get_soup(session, url):
    """Вспомогательная функция для получения объекта BeautifulSoup по указанному URL."""
    try:
        async with session.get(url) as response:
            if response.status == 200:
                html = await response.text()
                return BeautifulSoup(html, 'lxml')
            else:
                print(f'Ошибка при загрузке {url}, код состояния: {response.status}')
                return None
    except Exception as e:
        print(f'Исключение при загрузке {url}: {e}')
        return None

async def parse_product(session, url, writer):
    """Парсинг страницы отдельного продукта и запись данных в CSV."""
    soup = await get_soup(session, url)
    if soup:
        try:
            name = soup.select_one('p#p_header').text.strip()
            article = soup.select_one('p.article').text.split(': ')[1].strip()
            price = soup.select_one('span#price').text.strip()
            old_price = soup.select_one('span#old_price').text.strip()
            in_stock = soup.select_one('span#in_stock').text.split(': ')[1].strip()
            brand = soup.select_one('li#brand').text.split(': ')[1].strip()
            model = soup.select_one('li#model').text.split(': ')[1].strip()
            await writer.writerow([name, article, brand, model, in_stock, price, old_price])
            print('Спарсили: ', name, article, brand, model, in_stock, price, old_price)
        except AttributeError as e:
            print(f'Ошибка при парсинге деталей продукта с {url}: {e}')

async def parse_page(session, page_url, writer):
    """Парсинг всех продуктов на заданной странице."""
    soup = await get_soup(session, page_url)
    if soup:
        hrefs = [a.get('href') for a in soup.select('a.name_item')]
        tasks = [parse_product(session, f'{schema}{href}', writer) for href in hrefs]
        await asyncio.gather(*tasks)

async def parse_section(session, section_url, writer):
    """Парсинг всех страниц в пределах раздела."""
    soup = await get_soup(session, section_url)
    if soup:
        pagen_urls = [f"{schema}{link['href']}" for link in soup.find('div', class_='pagen').find_all('a')]
        tasks = [parse_page(session, page_url, writer) for page_url in pagen_urls]
        await asyncio.gather(*tasks)

async def main():
    async with aiohttp.ClientSession() as session:
        soup = await get_soup(session, url)
        if soup:
            nav_menu = [f"{schema}{link['href']}" for link in soup.find('div', class_='nav_menu').find_all('a')]
            async with aio_open('result.csv', mode='w', encoding='utf-8-sig', newline='') as file:
                writer = csv.writer(file, delimiter=';')
                await writer.writerow(['Наименование', 'Артикул', 'Бренд', 'Модель', 'Наличие', 'Цена', 'Старая цена'])
                tasks = [parse_section(session, section_url, writer) for section_url in nav_menu]
                await asyncio.gather(*tasks)

# Запуск основной функции
asyncio.run(main())
