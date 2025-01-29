from pyrogram import Client

api_id = 2********2
api_hash = "8*****************7"

app = Client("my_session", api_id=api_id, api_hash=api_hash)

chat_id = 'python_parsing'  # Например, можно использовать @username для публичных каналов или чатов
query = 'парсинг'           # Текст, который вы хотите найти в сообщениях
offset = 0                  # Смещение от начала списка сообщений (0 означает начало)
filter = None               # Тип фильтра (например, 'photo' для фото)
limit = 200                 # Максимальное количество сообщений, которое вы хотите получить
from_user = 'Pashikk'       # Если нужно искать сообщения только от конкретного пользователя


def main():
    with app:
        # Поиск сообщений
        messages = app.search_messages(chat_id=chat_id, query=query, offset=offset, limit=limit, from_user=from_user)
        # Вывод результатов
        for message in messages:
            # Вывод ID сообщения, имени его автора и текста
            print(f'message id: {message.id} from user: {message.from_user.username}, '
                  f'message text: {message.text}')  

main()

from pyrogram.enums import MessagesFilter

from pyrogram import Client
from pyrogram.enums import MessagesFilter

with Client("my_account") as app:
    # Пустой фильтр (любой тип сообщений)
    app.search_messages(chat_id="python_parsing", filter=MessagesFilter.EMPTY)

    # Сообщения с фотографиями
    app.search_messages(chat_id="python_parsing", filter=MessagesFilter.PHOTO)

    # Сообщения с видео
    app.search_messages(chat_id="python_parsing", filter=MessagesFilter.VIDEO)

    # Возвращает сообщения, содержащие либо фотографии, либо видео
    app.search_messages(chat_id="python_parsing", filter=MessagesFilter.PHOTO_VIDEO)

    # Возвращает сообщения, содержащие документы (например, PDF, DOCX)
    app.search_messages(chat_id="python_parsing", filter=MessagesFilter.DOCUMENT)

    # Сообщения, содержащие URL-адреса
    app.search_messages(chat_id="python_parsing", filter=MessagesFilter.URL)

    # Возвращает сообщения, содержащие анимации (обычно это GIF).
    app.search_messages(chat_id="python_parsing", filter=MessagesFilter.ANIMATION)

    # Сообщения с голосовыми заметками
    app.search_messages(chat_id="python_parsing", filter=MessagesFilter.VOICE_NOTE)

    # Сообщения с видеозаметками
    app.search_messages(chat_id="python_parsing", filter=MessagesFilter.VIDEO_NOTE)

    # Возвращает сообщения, содержащие аудио и видеозаметки
    app.search_messages(chat_id="python_parsing", filter=MessagesFilter.AUDIO_VIDEO_NOTE)

    # Аудиосообщения (музыка)
    app.search_messages(chat_id="python_parsing", filter=MessagesFilter.AUDIO)

    # Сообщения с фотографиями чата
    app.search_messages(chat_id="python_parsing", filter=MessagesFilter.CHAT_PHOTO)

    # Сообщения с телефонными звонками
    app.search_messages(chat_id="python_parsing", filter=MessagesFilter.PHONE_CALL)

    # Возвращает сообщения, в которых есть упоминания пользователя (через @username или если пользователь упомянут напрямую).
    app.search_messages(chat_id="python_parsing", filter=MessagesFilter.MENTION)

    # Сообщения с местоположением
    app.search_messages(chat_id="python_parsing", filter=MessagesFilter.LOCATION)

    # Сообщения с контактами
    app.search_messages(chat_id="python_parsing", filter=MessagesFilter.CONTACT)

    # Закрепленные сообщения
    app.search_messages(chat_id="python_parsing", filter=MessagesFilter.PINNED)

from pyrogram import Client
from pyrogram.enums import MessagesFilter

api_id = 2***********2
api_hash = "8*7"****************
app = Client("my_session", api_id=api_id, api_hash=api_hash)

def main():
    with app:
        group_url = "parsinger_pyrogram"

        # Возвращает сообщения, содержащие анимации (обычно это GIF).
        messages = app.search_messages(group_url, filter=MessagesFilter.ANIMATION)
        for message in messages:
            print(message)


main()