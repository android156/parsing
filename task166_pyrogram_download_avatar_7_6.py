import time

from pyrogram import Client
from pyrogram.enums import MessagesFilter
from tqdm import tqdm
import asyncio

import os

def calculate_directory_size(path):
    """
    Подсчитывает размер всех файлов в директории.

    :param path: Путь к директории, размер файлов которой нужно подсчитать.
    :return: Общий размер файлов в байтах.
    """
    total_size = 0
    for root, dirs, files in os.walk(path):
        for file in files:
            file_path = os.path.join(root, file)
            if os.path.isfile(file_path):
                total_size += os.path.getsize(file_path)
    return total_size

api_id = 25300378
api_hash = "b1d1f4c93bf8f885a884030878eaa9bc"
lock = asyncio.Lock()


group_url = 'parsinger_pyrogram'  # Например, можно использовать @username для публичных каналов или чатов

photo_files_list = []

async def download_photo(app, file_id, file_name):
    await app.download_media(file_id, file_name)

async def main():
    app = Client("my_session", api_id=api_id, api_hash=api_hash)
    async with app:
        sum = 0
        members = app.get_chat_members(chat_id=group_url, )
        async for member in members:
            print(member.user.id)
            await asyncio.sleep(2)
            member_photos = app.get_chat_photos(member.user.id)
            if member_photos:
                async for photo in member_photos:
                    file_name = f"photo/{photo.file_id}"
                    file_size = photo.file_size
                    # print(photo)
                    file_name += ".jpg"
                    async with lock:
                        photo_files_list.append((file_name, photo.file_id))
                        sum += file_size

        download_tasks = [asyncio.create_task(download_photo(app, file_id, file_name)) for file_name, file_id in photo_files_list]
        await asyncio.gather(*download_tasks)


        print('Теоретический размер папки:', sum)
    print('Реальный размер папки:', calculate_directory_size('photo/'))

asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
if __name__ == "__main__":
    asyncio.run(main())

# def calculate_directory_size(path):
#     """
#     Подсчитывает размер всех файлов в директории.
#
#     :param path: Путь к директории, размер файлов которой нужно подсчитать.
#     :return: Общий размер файлов в байтах.
#     """
#     total_size = 0
#     for root, dirs, files in os.walk(path):
#         for file in files:
#             file_path = os.path.join(root, file)
#             if os.path.isfile(file_path):
#                 total_size += os.path.getsize(file_path)
#     print(total_size)
#     return total_size
#
#
# async def download_avatar(client, user):
#     # Проверяем, есть ли у пользователя аватарка
#     if user.photo:
#         file_path = f"avatars/{user.id}.jpg"  # Путь для сохранения аватарки
#         # Скачиваем аватарку
#         await client.download_media(user.photo.big_file_id, file_path)
#
#
# async def main():
#     current_directory = os.getcwd()
#
#     async with app:
#         # Создаем папку для сохранения аватарок, если её еще нет
#         if not os.path.exists("avatars"):
#             os.makedirs("avatars")
#
#         # Получаем список всех пользователей в чате
#         async for member in app.get_chat_members(group_url):
#             # print(member)
#             # Скачиваем аватарку каждого пользователя
#             await download_avatar(app, member.user)
#
#     calculate_directory_size(current_directory)
#
#
# # Запускаем основную функцию
# app.run(main())

# ****************************************************************
# ****************************************************************
# ****************************************************************

# from pyrogram import Client
# from api_info import API_ID, API_HASH
# from tqdm import tqdm
# import os
#
# group_url = "parsinger_pyrogram"
# app = Client("my_session", api_id=API_ID, api_hash=API_HASH)
#
# # Создание директории media в папке проектов, если она не существует
# # если уже существует, то будет осуществлена перезапись всех файлов в эту папку
# os.makedirs('media', exist_ok=True)
#
#
# def progress(current, total, progress_bar):
#     # Обновляем прогресс-бар
#     progress_bar.update(current - progress_bar.n)
#
#
# def calculate_directory_size(path):
#     """
#     Подсчитывает размер всех файлов в директории.
#     :param path: Путь к директории, размер файлов которой нужно подсчитать.
#     :return: Общий размер файлов в байтах.
#     """
#     total_size = 0
#     for root, dirs, files in os.walk(path):
#         for file in files:
#             file_path = os.path.join(root, file)
#             if os.path.isfile(file_path):
#                 total_size += os.path.getsize(file_path)
#     return total_size
#
#
# def main():
#     with app:
#         # Получаем список всех участников группы и их id
#         members = app.get_chat_members(group_url)
#         for member in members:
#             # для каждого участника по номеру id его находим объект chat_photos, в котором находятся
#             # несколько фотографий профиля участника: большая аватарка с file_id и две
#             # маленьких фотографий thumbs, для задачи нужно выбрать большую фотографию
#             chat_photos = app.get_chat_photos(member.user.id)
#             for photo in chat_photos:
#                 # print(photo)
#                 # Скачиваем большую фотографию профиля, для имени фото проще указать id участника
#                 file_name = f"media/{member.user.id}.jpg"
#                 app.download_media(photo.file_id, file_name=file_name)
#
# main()
#
# filepath = r'D:\Python\Parcer\media'
# result = calculate_directory_size(filepath)
# print('result =', result)
#
# '''
# структура объекта photo
#
# {
#     "_": "Photo",
#     "file_id": "AgACAgIAAxUAAWdt7Z0tMhTR9w47AotF1vbyBOqwAAK2pzEbXKXUEza4IVlOYG6NAAgBAAMCAANjAAceBA",
#     "file_unique_id": "AgADtqcxG1yl1BM",
#     "width": 640,
#     "height": 640,
#     "file_size": 60361,
#     "date": "2024-12-06 16:07:52",
#     "thumbs": [
#         {
#             "_": "Thumbnail",
#             "file_id": "AgACAgIAAxUAAWdt7Z0tMhTR9w47AotF1vbyBOqwAAK2pzEbXKXUEza4IVlOYG6NAAgBAAMCAANhAAceBA",
#             "file_unique_id": "AgADtqcxG1yl1BM",
#             "width": 160,
#             "height": 160,
#             "file_size": 6153
#         },
#         {
#             "_": "Thumbnail",
#             "file_id": "AgACAgIAAxUAAWdt7Z0tMhTR9w47AotF1vbyBOqwAAK2pzEbXKXUEza4IVlOYG6NAAgBAAMCAANiAAceBA",
#             "file_unique_id": "AgADtqcxG1yl1BM",
#             "width": 320,
#             "height": 320,
#             "file_size": 18573
#         }
#     ]
# }
# ...
#
# result = 2338941
# '''


# import asyncio
# import os
#
# from pyrogram import Client
# from pyrogram.types import ChatMember
#
# from config import API_ID, API_HASH, GROUP_NAME
#
#
# async def calculate_directory_size(path: str) -> int:
#     total_size = 0
#     for root, dirs, files in os.walk(path):
#         for file in files:
#             file_path = os.path.join(root, file)
#             if os.path.isfile(file_path):
#                 total_size += os.path.getsize(file_path)
#     return total_size
#
#
# async def downloader(app: Client, member: ChatMember, path: str) -> None:
#     chat_member_photos = app.get_chat_photos(member.user.id)
#     async for photo in chat_member_photos:
#         await app.download_media(photo, file_name=f"{path}{member.user.photo.big_photo_unique_id}.jpg")
#
#
# async def main() -> None:
#     async with Client(name="my_session", api_id=API_ID, api_hash=API_HASH) as app:
#         path = "media/"
#         tasks = [
#             downloader(app, member, path)
#             async for member in app.get_chat_members(GROUP_NAME)
#         ]
#         await asyncio.gather(*tasks)
#         result = await calculate_directory_size(path)
#
#         print(result)
#
#
# if __name__ == "__main__":
#     loop = asyncio.get_event_loop()
#     loop.run_until_complete(main())
