from pyrogram import Client
from pyrogram.enums import MessagesFilter


api_id = 25300378
api_hash = "b1d1f4c93bf8f885a884030878eaa9bc"

app = Client("my_session", api_id=api_id, api_hash=api_hash)

chat_id = 'parsinger_pyrogram'  # Например, можно использовать @username для публичных каналов или чатов
query = 'http'           # Текст, который вы хотите найти в сообщениях
offset = 0                  # Смещение от начала списка сообщений (0 означает начало)
filter=MessagesFilter.CONTACT           # Тип фильтра (например, 'photo' для фото)
limit = 200                 # Максимальное количество сообщений, которое вы хотите получить
from_user = 'Pashikk'       # Если нужно искать сообщения только от конкретного пользователя


def main():
    with app:
        users_id_set = set()
        # Поиск сообщений
        messages = app.get_chat_history(chat_id=chat_id)
        # Вывод результатов
        for message in messages:
            if message.reply_to_message_id:
                reply_to_message = app.get_messages(chat_id=chat_id, message_ids=message.reply_to_message_id)
                try:
                    print(f'message id: {message.id} reply_to_message_id: {message.reply_to_message_id}, '
                          f'user_reply_to_message_id: {reply_to_message.from_user.id}')
                    users_id_set.add(reply_to_message.from_user.id)
                except AttributeError:
                    strange_messages =
                    print(message.id, message.reply_to_message_id)
        print(f'sum: {sum(users_id_set)}')

main()

# from pyrogram.enums import MessagesFilter
#
# from pyrogram import Client
# from pyrogram.enums import MessagesFilter
#
# with Client("my_account") as app:
#     # Пустой фильтр (любой тип сообщений)
#     app.search_messages(chat_id="python_parsing", filter=MessagesFilter.EMPTY)
#
#     # Сообщения с фотографиями
#     app.search_messages(chat_id="python_parsing", filter=MessagesFilter.PHOTO)
#
#     # Сообщения с видео
#     app.search_messages(chat_id="python_parsing", filter=MessagesFilter.VIDEO)
#
#     # Возвращает сообщения, содержащие либо фотографии, либо видео
#     app.search_messages(chat_id="python_parsing", filter=MessagesFilter.PHOTO_VIDEO)
#
#     # Возвращает сообщения, содержащие документы (например, PDF, DOCX)
#     app.search_messages(chat_id="python_parsing", filter=MessagesFilter.DOCUMENT)
#
#     # Сообщения, содержащие URL-адреса
#     app.search_messages(chat_id="python_parsing", filter=MessagesFilter.URL)
#
#     # Возвращает сообщения, содержащие анимации (обычно это GIF).
#     app.search_messages(chat_id="python_parsing", filter=MessagesFilter.ANIMATION)
#
#     # Сообщения с голосовыми заметками
#     app.search_messages(chat_id="python_parsing", filter=MessagesFilter.VOICE_NOTE)
#
#     # Сообщения с видеозаметками
#     app.search_messages(chat_id="python_parsing", filter=MessagesFilter.VIDEO_NOTE)
#
#     # Возвращает сообщения, содержащие аудио и видеозаметки
#     app.search_messages(chat_id="python_parsing", filter=MessagesFilter.AUDIO_VIDEO_NOTE)
#
#     # Аудиосообщения (музыка)
#     app.search_messages(chat_id="python_parsing", filter=MessagesFilter.AUDIO)
#
#     # Сообщения с фотографиями чата
#     app.search_messages(chat_id="python_parsing", filter=MessagesFilter.CHAT_PHOTO)
#
#     # Сообщения с телефонными звонками
#     app.search_messages(chat_id="python_parsing", filter=MessagesFilter.PHONE_CALL)
#
#     # Возвращает сообщения, в которых есть упоминания пользователя (через @username или если пользователь упомянут напрямую).
#     app.search_messages(chat_id="python_parsing", filter=MessagesFilter.MENTION)
#
#     # Сообщения с местоположением
#     app.search_messages(chat_id="python_parsing", filter=MessagesFilter.LOCATION)
#
#     # Сообщения с контактами
#     app.search_messages(chat_id="python_parsing", filter=MessagesFilter.CONTACT)
#
#     # Закрепленные сообщения
#     app.search_messages(chat_id="python_parsing", filter=MessagesFilter.PINNED)
#
# from pyrogram import Client
# from pyrogram.enums import MessagesFilter
#
# api_id = 2***********2
# api_hash = "8*7"****************
# app = Client("my_session", api_id=api_id, api_hash=api_hash)
#
# def main():
#     with app:
#         group_url = "parsinger_pyrogram"
#
#         # Возвращает сообщения, содержащие анимации (обычно это GIF).
#         messages = app.search_messages(group_url, filter=MessagesFilter.ANIMATION)
#         for message in messages:
#             print(message)
#
#
# main()