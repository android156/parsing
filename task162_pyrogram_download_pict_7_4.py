from pyrogram import Client
from pyrogram.enums import MessagesFilter
from tqdm import tqdm

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

app = Client("my_session", api_id=api_id, api_hash=api_hash)

group_url = 'parsinger_pyrogram'  # Например, можно использовать @username для публичных каналов или чатов

def progress(current, total, progress_bar):
    # Обновляем прогресс-бар
    progress_bar.update(current - progress_bar.n)

def main():
    with app:
        sum = 0
        for message in app.get_chat_history(group_url):
            if message.media:
                file_name = f"media2/{message.id}"
                file_size = None

                # Определение расширения файла и размера в зависимости от типа медиа
                if message.photo:
                    file_name += ".jpg"
                    file_size = message.photo.file_size



                # Создание прогресс-бара для каждого файла
                # Если размер файла определен, создаем прогресс-бар и начинаем загрузку
                if file_size:
                    with tqdm(total=file_size, unit='B', unit_scale=True, desc="Скачивание") as progress_bar:
                        app.download_media(message, file_name=file_name, progress=progress, progress_args=(progress_bar,))
                    sum += file_size
        print('Теоретический размер папки:', sum)
    print('Реальный размер папки:',calculate_directory_size('media2/'))

if __name__ == '__main__':
    main()


# Асинхронная скачка с телеги
# import time
# import asyncio
# from pyrogram import Client
# from pyrogram.enums import MessagesFilter
# from pypyro import api_id, api_hash
# import aiofiles
#
# group_url = "parsinger_pyrogram"
#
# async def download_to_buffer(app, message, buffer):
#     """Скачиваем файл в буфер."""
#     try:
#         await asyncio.sleep(0)
#         file_like_object = await app.download_media(message.photo, in_memory=True)
#         if file_like_object is not None:
#             buffer[message.id] = file_like_object
#             print(f"Файл {message.id}.jpg загружен в буфер.")
#         else:
#             print(f"Ошибка: файл {message.id} не был загружен.")
#     except Exception as e:
#         print(f"Ошибка при загрузке {message.id}: {e}")
#
# async def save_to_disk(buffer):
#     """Сохраняем файлы из буфера на диск."""
#     for message_id, file_like_object in buffer.items():
#         try:
#             async with aiofiles.open(f'downloads/photos/{message_id}.jpg', 'wb') as f:
#                 await f.write(file_like_object.getbuffer())
#             print(f"Файл {message_id}.jpg сохранён на диск.")
#         except Exception as e:
#             print(f"Ошибка при сохранении {message_id}: {e}")
#
# async def main():
#     async with Client("session_nawme5", api_id=api_id, api_hash=api_hash) as app:
#         semaphore = asyncio.Semaphore(12)  # Ограничение одновременных скачиваний
#         buffer = {}  # Словарь для хранения файлов в буфере
#
#         # Получаем сообщения с фотографиями
#         messages = [message async for message in app.search_messages(chat_id=group_url, filter=MessagesFilter.PHOTO)]
#
#         # Скачиваем файлы в буфер
#         download_tasks = [
#             download_to_buffer(app, message, buffer)
#             for message in messages[:12]
#         ]
#         start_g = time.time()
#         await asyncio.gather(*download_tasks)
#         print(f"Все файлы загружены в буфер за {time.time() - start_g:.2f} секунд.")
#
#         # Сохраняем файлы на диск
#         start_s = time.time()
#         await save_to_disk(buffer)
#         print(f"Все файлы сохранены на диск за {time.time() - start_s:.2f} секунд.")
#
# # Запуск асинхронного кода
# asyncio.run(main())
#
# "установка атрибута block=False автоматически добавляет задачу в текущий цикл событий. Поэтому у Вас как будто создаётся список задач, который потом распаковывается в цикл событий, а в каждой из этих задач опять в цикл накидывается текущая задача."
# Можете пояснить подробнее?
# В моем старом варианте создается несколько задач
# tasks = [downloader(app, message, semaphore) for message in messages[:12]]
# которые затем запускаются на конкурентное выполнение в await asyncio.gather(*tasks)