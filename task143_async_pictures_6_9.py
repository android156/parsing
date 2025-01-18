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
        if resp.ok:
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
        else:
            print('Статус говно', resp.status)
        return None


async def write_file(session, url, name_img):
    async with semaphore:
        async with aiofiles.open(f'images3/{name_img}', mode='wb') as f:
            async with session.get(url) as response:
                async for x in response.content.iter_chunked(1024):
                    await f.write(x)
            print(f'Изображение сохранено {name_img}')


async def main(domain):
    connector = aiohttp.TCPConnector(limit_per_host=10)
    url = domain + 'index.html'
    async with aiohttp.ClientSession(connector=connector) as session:
        async with session.get(url) as response:
            urls = await get_list_urls(session, url, 'a.lnk_img')
            url_tasks = [asyncio.create_task(get_list_urls(session, url, 'a.lnk_img')) for url in urls]
            urls2 = flatten_list(await asyncio.gather(*url_tasks))
            img_url_tasks = [asyncio.create_task(get_list_urls(session, url, 'img.picture')) for url in urls2]
            img_urls = flatten_list(await asyncio.gather(*img_url_tasks))

            get_img_tasks = []
            img_names = []
            for url in img_urls:
                name_img = url.split('/')[-1]
                if name_img not in img_names:
                    task = asyncio.create_task(write_file(session, url, name_img))
                    get_img_tasks.append(task)
                    img_names.append(name_img)
            await asyncio.gather(*get_img_tasks)


domain = 'https://parsinger.ru/asyncio/aiofile/3/'
start = time.perf_counter()
asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
semaphore = asyncio.Semaphore(50)
asyncio.run(main(domain))
print(f'Cохранено изображений {len(os.listdir("images3/"))} за {round(time.perf_counter() - start, 3)} сек')
print(get_folder_size('images3/'))
# Cохранено изображений 2615 за 74.991 сек
