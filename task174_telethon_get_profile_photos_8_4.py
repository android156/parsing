import datetime
from api_info import API_ID, API_HASH
from telethon import TelegramClient, events, sync, connection
import asyncio
import pyperclip
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

url = 't.me/Parsinger_Telethon_Test'

with TelegramClient('session_name2', API_ID, API_HASH, system_version="5.10.7 beta x64") as client:
    participants = client.get_participants(url)

    print('participants =', participants)
    for i, user in enumerate(participants):
        for j, iter_photo in enumerate(client.iter_profile_photos(user)):
            print(f'Working on photo {i}_{j}...')
            client.download_media(iter_photo, f'tele_avatars/{i}_{j}')



print('Реальный размер папки:', calculate_directory_size('tele_avatars/'))

# from telethon import TelegramClient, events, sync, connection

# r_api = 1*******8
# r_hash = 'b4******************b'
#
# with TelegramClient('my', r_api, r_hash) as client:
#     all_user_group = client.get_participants('t.me/Parsinger_Telethon_Test')
#     for user in all_user_group:
#         for iter_photo in client.iter_profile_photos(user):
#             client.download_media(iter_photo, file='img/')