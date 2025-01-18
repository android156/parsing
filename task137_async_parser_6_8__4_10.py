# Для запуска этого кода потребуются рабочие прокси.
import time

import aiohttp
import asyncio
import requests
from bs4 import BeautifulSoup
from aiohttp_socks import ChainProxyConnector
from aiohttp_retry import RetryClient, ExponentialRetry
from fake_useragent import UserAgent

category_lst = []
pagen_lst = []
domain = 'http://parsinger.ru/html/'
lock = asyncio.Lock()

def get_soup(url):
    resp = requests.get(url=url)
    return BeautifulSoup(resp.text, 'lxml')


def get_urls_categories(soup):
    all_link = soup.find('div', class_='nav_menu').find_all('a')

    for cat in all_link:
        category_lst.append(domain + cat['href'])


def get_urls_pages(category_lst):
    # Заносит ссылки на все страницы в категориях в общий список pagen_lst
    for cat in category_lst:
        soup = get_soup(cat)
        for pagen in soup.find('div', class_='pagen').find_all('a'):
            pagen_lst.append(domain + pagen['href'])


async def get_data(session, link):
    total = 0
    retry_options = ExponentialRetry(attempts=2)
    retry_client = RetryClient(raise_for_status=False, retry_options=retry_options, client_session=session,
                               start_timeout=0.5)
    async with retry_client.get(link) as response:
        if response.ok:
            resp = await response.text()
            soup = BeautifulSoup(resp, 'lxml')
            item_card = [x['href'] for x in soup.find_all('a', class_='name_item')]
            for item_url in item_card:
                full_url = domain + item_url
                async with session.get(url=full_url) as response2:
                    resp2 = await response2.text()
                    soup2 = BeautifulSoup(resp2, 'lxml')
                    in_stock = int(soup2.find('span', id='in_stock').text.split(': ')[1])
                    price = int(soup2.find('span', id='price').text.split(' ')[0])
                    old_price = int(soup2.find('span', id='old_price').text.split(' ')[0])
                    async with lock:
                        total += (old_price - price) * in_stock
    return total


async def main():
    disc_sum = 0
    ua = UserAgent()
    fake_ua = {'user-agent': ua.random}
    connector = ChainProxyConnector.from_urls(
        [
            'socks5://TdWubd:s914RN@5.101.91.200:8000',
            'socks5://TdWubd:s914RN@5.8.60.177:8000',

        ]
    )
    async with aiohttp.ClientSession(connector=connector, headers=fake_ua) as session:
        tasks = []
        for link in pagen_lst:
            task = asyncio.create_task(get_data(session, link))
            tasks.append(task)
        results = await asyncio.gather(*tasks)
        disc_sum = sum(results)
    return disc_sum

url = 'https://parsinger.ru/html/index1_page_1.html'
soup = get_soup(url)
get_urls_categories(soup)
get_urls_pages(category_lst)

asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
start = time.time()
print(asyncio.run(main()))
print(f'время: {time.time() - start}')