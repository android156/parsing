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


async def get_img_urls(session, url):
    async with session.get(url) as resp:
        soup = BeautifulSoup(await resp.text(), 'lxml')
        images = soup.select('img.picture')
        img_urls = [img.get('src') for img in images]
        return img_urls


async def write_file(session, url, name_img):
    async with aiofiles.open(f'images2/{name_img}', mode='wb') as f:
        async with session.get(url) as response:
            async for x in response.content.iter_chunked(1024):
                await f.write(x)
        print(f'Изображение сохранено {name_img}')


async def main(domain):
    url = domain + 'index.html'
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            soup = BeautifulSoup(await response.text(), 'lxml')
            urls = [f'{domain}{x["href"]}' for x in soup.select('a.lnk_img')]
            img_url_tasks = [asyncio.create_task(get_img_urls(session, url)) for url in urls]
            img_urls_lists = await asyncio.gather(*img_url_tasks)
            img_urls = [url for img_url_list in img_urls_lists for url in img_url_list]
            get_img_tasks = []
            for url in img_urls:
                name_img = url.split('/')[-1]
                task = asyncio.create_task(write_file(session, url, name_img))
                get_img_tasks.append(task)
            await asyncio.gather(*get_img_tasks)


domain = 'https://parsinger.ru/asyncio/aiofile/2/'
start = time.perf_counter()
asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
asyncio.run(main(domain))
print(f'Cохранено изображений {len(os.listdir("images2/"))} за {round(time.perf_counter() - start, 3)} сек')
print(get_folder_size('images2/'))
# Результат Cохранено 100 изображений за 7.732 сек
