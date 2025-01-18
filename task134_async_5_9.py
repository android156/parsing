import asyncio
import time
import aiohttp
from bs4 import BeautifulSoup

# ---------------------start block 1------------------------
category = ['watch', 'mobile', 'mouse', 'hdd', 'headphones']
urls = [f'https://parsinger.ru/html/{cat}/{i}/{i}_{x}.html' for cat, i in zip(category, range(1, len(category) + 1)) for
        x in range(1, 33)]
# ---------------------end block 1------------------------

# ---------------------start block 2------------------------
async def run_tasks(url, session):
    async with session.get(url) as resp:
        soup = BeautifulSoup(await resp.text(), 'lxml')
        price = soup.find('span', id='price').text
        name = soup.find('p', id='p_header').text
        print(resp.url, price, name)
# ---------------------end block 2------------------------

# ---------------------start block 3------------------------
async def main():
    async with aiohttp.ClientSession() as session:
        tasks = [run_tasks(link, session) for link in urls]
        await asyncio.gather(*tasks)
# ---------------------end block 3------------------------

# ---------------------start block 4------------------------

if __name__ == '__main__':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    start = time.time()
    asyncio.run(main())
    print(time.time()-start)


# async def run_tasks(url, session):
#     async with session.get(url) as resp:
#         soup = BeautifulSoup(await resp.text(), 'lxml')
#         price = soup.find('span', id='price').text
#         name = soup.find('p', id='p_header').text
#         return resp.url, price, name
#
# А в main() сохраним результаты работы всех задач в список result и распечатаем содержимое этого списка:
#
# async def main():
#     async with aiohttp.ClientSession() as session:
#         tasks = [run_tasks(link, session) for link in urls]
#         # Сохраняем результаты работы всех задач в result
#         result = await asyncio.gather(*tasks)
#         # Распечатываем содержимое списка result
#         for x in result:
#             print(*x, sep=', ')