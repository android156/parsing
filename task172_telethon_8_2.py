from telethon import TelegramClient, events, sync, connection
import asyncio

api_id = 25300378
api_hash = "b1d1f4c93bf8f885a884030878eaa9bc"

client = TelegramClient('session_name', api_id, api_hash, system_version="4.10.5 beta x64")
client.start()
print(client.get_me())
client.disconnect()



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