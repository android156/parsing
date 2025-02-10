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
    participant_list = []
    print('participants =', participants)
    for item in participants:
        print(item.id, item.first_name, item.last_name, item.phone)
        participant_list.append(f'{item.id} {item.first_name} {item.last_name} {item.phone}')
    print(participant_list)
    for i, user in enumerate(participants):
        client.download_profile_photo(user, f'tele_avatars/{i}', download_big=True)  # f'img/{i}' используйте для указания пути сохранения файлов
    pyperclip.copy(participant_list)

print('Реальный размер папки:', calculate_directory_size('tele_avatars/'))
#
# [User(id=332703068,
#       is_self=True,
#       contact=True,
#       mutual_contact=True,
#       deleted=False, bot=False,
#       bot_chat_history=False,
#       bot_nochats=False,
#       verified=False,
#       restricted=False,
#       min=False,
#       bot_inline_geo=False,
#       support=False, scam=False,
#       apply_min_photo=False, fake=False,
#       access_hash=-5964566557575375003,
#       first_name='Павел', last_name='Хошев',
#       username='Pashikk',
#       phone='79384757505',
#       photo=UserProfilePhoto(
#           photo_id=1428948796795103153,
#           dc_id=2, has_video=False,
#           stripped_thumb=b'\x01\x08\x08I\xb5\x12\xe4\xed\x90\x8c\xf1\x81\xe9E\x14Qa3'),
#       status=UserStatusOffline(was_online=datetime.datetime(2022, 6, 11, 12, 57, 19,
#                                                             tzinfo=datetime.timezone.utc)),]
#  ........
#


#
# from telethon import TelegramClient
#
# # Укажите свои api_id и api_hash
# api_id = 'YOUR_API_ID'
# api_hash = 'YOUR_API_HASH'
#
# client = TelegramClient("my_session", api_id, api_hash)
#
# async def main():
#     await client.start()
#
#     # Указываем чат (по username или chat_id)
#     chat_username = 'Parsinger_Telethon_Test'  # или укажите ID чата
#     participants = await client.get_participants(chat_username)
#
#     # Перебираем участников и выводим информацию о каждом
#     for user in participants:
#         print(f"Username: {user.username}, ID: {user.id}, Имя: {user.first_name}")
#
# # Запускаем асинхронную функцию
# with client:
#     client.loop.run_until_complete(main())
#

# # Создание клиента и использование его в блоке with
# async with TelegramClient('anon', api_id, api_hash) as client:
#     me = await client.get_me()
#     print(me.stringify())

#
#
#     User(
#         id=332703068 - id пользователя;
#         is_self=True - возвращает True, если запрос был отправлен "О себе", возвращает False в противоположном случае;
#         contact=True - возвращает True, если пользователь есть в вашем списке контактов, возвращает False в противоположном случае;
#         mutual_contact=True - возвращает True, если пользователи взаимно подписаны друг на друга(есть у друг друга в контактах), возвращает False в противоположном случае;
#         deleted=False - возвращает True, если аккаунт пользователя был удален, False, если аккаунт активен;
#         bot=False  -  возвращает True, если аккаунт является ботом, возвращает False в противоположном случае;
#         bot_chat_history=False -  возвращает True, если данный бот умеет читать сообщения в группе, возвращает False в противоположном случае;
#         bot_nochats=False  -  возвращает True, если бота можно добавить в группу, возвращает False в противоположном случае;
#         verified=False- возвращает True, если пользователь верифицирован при помощи смс, ", возвращает False в противоположном случае;
#          restricted=False - возвращает True, если пользователь находится в вашем чёрном списке, возвращает False в противоположном случае;
#             min=False - параметр указывает на полноту представляемых данных. False означает, что объект User содержит полную информацию о пользователе. Например, когда вы взаимодействуете с аккаунтом, к которому у вас есть прямой доступ, или используете метод, возвращающий полный набор данных.
#         min=True может автоматически устанавливаться Telegram API, например, при получении данных о пользователе через публичный чат или канал, где Telegram предоставляет минимальную информацию.
#         bot_inline_geo=False -  возвращает True, если бот может запрашивать вашу геолокацию.
#         support=False  -  возвращает True, если пользователь является официальным пользователем поддержки, возвращает False в противоположном случае;
#         scam=False - возвращает True, если на пользователя было отправлено множество жалоб о мошенничестве(нигде нет инфы о том, сколько конкретно должно быть жалоб), возвращает False в противоположном случае;
#         apply_min_photo=False  - возвращает True, если у пользователя установлено фото профиля, возвращает False в противоположном случае;
#         fake=False- возвращает True, если множество пользователей пожаловались о том, что аккаунт фейковый( не известно отличие от scam=False), возвращает False в противоположном случае;
#         access_hash=-5**4**6**7**5**5**3 - возвращает хэш доступа пользователя;
#         first_name='Павел' - возвращает first_name пользователя;
#         last_name='Хошев' - возвращает last_name пользователя;
#         username='Pashikk' - возвращает username пользователя;
#         phone='7**8***7**5'   - возвращает phone пользователя, если он не скрыт в настройках конфиденциальности;
#         photo=UserProfilePhoto( - вложенный кортеж c фото пользователя, если оно есть;
#             photo_id=1428948796795103153 - id фото пользователя;
#             dc_id=2 - идентификатор DC, где хранится фото пользователя;
#             has_video=False -  возвращает True, если у пользователя анимированная аватарка, возвращает False в противоположном случае;;
#             stripped_thumb=b'\x01\x08\x08I\xb5\x12\xe4\xed\x90\x8c\xf1\x81\xe9E\x14Qa3' ) - обрезанная миниатюра, хранится в байтовом виде и может быть скачана;
#         status=UserStatusOffline(was_online=datetime.datetime(2022, 6, 11, 11, 57, 8, tzinfo=datetime.timezone.utc)) - онлайн-статус пользователя(когда был онлайн последний раз);
#         bot_info_version=None - если пользователь - бот, будет отображена его версия;
#         restriction_reason=[ ]  - содержится причина, по которой пользователь был ограничен для вас;
#         bot_inline_placeholder=None - строка текста для бота по умолчанию;
#         lang_code=None)  - код языка пользователя.

#