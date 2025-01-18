import time
import asyncio
import aiohttp
from aiohttp_retry import RetryClient, ExponentialRetry

# Последние 2 ссылки — 404-е, добавлены в демонстрационных целях
links = ['https://parsinger.ru/html/watch/1/1_1.html',
         'https://parsinger.ru/html/watch/1/1_2.html',
         'https://parsinger.ru/html/watch/1/1_3.html',
         'https://parsinger.ru/html/watch/8/1_3.html',
         'https://parsinger.ru/html/watch/8/2_3.html']


# Корутина для вывода сообщения вида link:response.status
async def get_data(retry_client, link):
    async with retry_client.get(link) as response:
        print(f'{link}:{response.status}')


# Базовая корутина
async def main():
    async with aiohttp.ClientSession() as client_session:
        # statuses=[404] выбран для демонстрации, на практике
        # повторное обращение к несуществующей странице скорее всего бессмысленно
        retry_options = ExponentialRetry(attempts=4, statuses={404})
        async with RetryClient(
                raise_for_status=False, retry_options=retry_options,
                client_session=client_session, max_timeout=2.0) as retry_client:
            await asyncio.gather(*[get_data(retry_client, link) for link in links])


if __name__ == '__main__':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    start = time.time()
    asyncio.run(main())
    print(f'время: {time.time() - start}')