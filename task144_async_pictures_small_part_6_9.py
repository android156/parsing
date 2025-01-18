import time
import aiofiles
import asyncio
import aiohttp
from bs4 import BeautifulSoup
import os


def get_folder_size(filepath, size=0):
    for root, dirs, files in os.walk(filepath):
        for f in files:
            size += os.path.getsize(os.path.join(root, f))
    return size


def flatten_list(list_of_lists):
    return [el for sublist in list_of_lists for el in sublist]


async def get_list_urls(session, url, selector):
    async with session.get(url) as resp:
        soup = BeautifulSoup(await resp.text(), 'lxml')
        item_list = soup.select(selector)
        if item_list:
            if selector.split('.')[0] == 'img':
                atr = 'src'
                urls_list = [item.get(atr) for item in item_list]
            else:
                atr = 'href'
                if url.endswith('index.html'):
                    domain = '/'.join(url.split('/')[:-1])
                else:
                    domain = '/'.join(url.split('/')[:-1])
                urls_list = [f'{domain}/{item.get(atr)}' for item in item_list]
            return urls_list
        print(url, selector, item_list)
        return None





async def write_file(session, url, name_img):
    async with aiofiles.open(f'images3/{name_img}', mode='wb') as f:
        async with session.get(url) as response:
            async for x in response.content.iter_chunked(1024):
                await f.write(x)
        print(f'Изображение сохранено {name_img}')



# https://parsinger.ru/asyncio/aiofile/3/index.html
#       depth2/category4.html
# https://parsinger.ru/asyncio/aiofile/3/depth2/category1.html
# https://parsinger.ru/asyncio/aiofile/3/depth2/category2.html
#           html_in_img/img293.html
# https://parsinger.ru/asyncio/aiofile/3/depth2/html_in_img/img11.html
# https://parsinger.ru/asyncio/aiofile/3/depth2/html_in_img/img12.html
# https://parsinger.ru/asyncio/aiofile/3/depth2/html_in_img/img17.html


async def main(domain):
    url = 'https://parsinger.ru/asyncio/aiofile/3/depth2/html_in_img/img611.html'
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            img_urls = await get_list_urls(session, url, selector='img.picture')

            get_img_tasks = []
            for url in img_urls:
                name_img = url.split('/')[-1]
                task = asyncio.create_task(write_file(session, url, name_img))
                get_img_tasks.append(task)
            await asyncio.gather(*get_img_tasks)


domain = 'https://parsinger.ru/asyncio/aiofile/3/'
start = time.perf_counter()
asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
asyncio.run(main(domain))
print(f'Cохранено изображений {len(os.listdir("images3/"))} за {round(time.perf_counter() - start, 3)} сек')
print(get_folder_size('images2/'))
# Результат Cохранено 100 изображений за 7.732 сек
