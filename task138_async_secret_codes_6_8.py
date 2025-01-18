# Для запуска этого кода потребуются рабочие прокси.
import time

import aiohttp
import asyncio
import requests
from bs4 import BeautifulSoup
from aiohttp_socks import ChainProxyConnector
from aiohttp_retry import RetryClient, ExponentialRetry
from fake_useragent import UserAgent


def get_soup(url):
    resp = requests.get(url=url)
    return BeautifulSoup(resp.text, 'lxml')


def get_all_links(soup):
    all_links = soup.find('div', class_='item_card').find_all('a')
    return [f"{domain}{link['href']}" for link in all_links]


semaphore = asyncio.Semaphore(20)
domain = 'https://parsinger.ru/asyncio/create_soup/1/'


async def get_data(session, link):
    async with semaphore:
        retry_options = ExponentialRetry(attempts=2, max_timeout=150, statuses={301, 302})
        retry_client = RetryClient(raise_for_status=False, retry_options=retry_options, client_session=session,
                                   start_timeout=0.5)
        async with retry_client.get(link) as response:
            # print(asyncio.current_task().get_name(), link)
            print(response.status)
            if response.ok:
                print('Эта рабочая!')
                soup = BeautifulSoup(await response.text(), 'lxml')
                res = soup.find('p', class_='text')
                return int(res.text)


async def main(url_list):
    ua = UserAgent()
    fake_ua = {'user-agent': ua.random}
    connector = ChainProxyConnector.from_urls(
        urls=[
            'socks5://TdWubd:s914RN@5.101.91.200:8000',
            'socks5://TdWubd:s914RN@5.8.60.177:8000',

        ],
        limit=100,
    )
    async with aiohttp.ClientSession(connector=connector, headers=fake_ua) as session:
        get_link_info_tasks = []
        for i, link in enumerate(url_list, 1):
            task = asyncio.create_task(get_data(session, link), name=f'{i}')
            get_link_info_tasks.append(task)
        results = await asyncio.gather(*get_link_info_tasks)
        return sum([_ for _ in results if _])


soup = get_soup('https://parsinger.ru/asyncio/create_soup/1/index.html')
asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
start = time.time()
print(asyncio.run(main(get_all_links(soup))))
print(f'время: {time.time() - start}')
