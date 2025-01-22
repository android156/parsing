from pyrogram import Client

api_id = 25300378
api_hash = "b1d1f4c93bf8f885a884030878eaa9bc"
group_url = "python_parsing"
app = Client("my_session", api_id=api_id, api_hash=api_hash)


# 1. Получить информацию о чате

def main():
    with app:
        group_url = "parsinger_pyrogram"
        chat = app.get_chat(group_url)
        print("Chat Info:", chat)

main()

# app.get_chat_members(chat_id, query, limit, filter): Получает список участников чата или группы.
#
#     chat_id(int | str)- Идентификатор или имя пользователя чата. Это может быть:
#         Целое число для идентификатора чата.
#         Строка с именем пользователя или ссылкой на чат (например, "@username" или "https://t.me/joinchat/...").
#
#     query(str, по умолчанию "") - Строка поиска для фильтрации участников чата. Если строка не пустая, будут
#     возвращены только участники, чьи имена или имена пользователей соответствуют запросу.
#
#     limit(int, по умолчанию 0) - Максимальное количество участников для возврата. Если значение равно 0, будут
#     возвращены все участники.
#
#     filter(enums.ChatMembersFilter.SEARCH): - Фильтр для применения при поиске участников. Это значение из
#     перечисления ChatMembersFilter, которое может включать в себя различные типы участников, такие как администраторы,
#     участники и так далее. По умолчанию используется ChatMembersFilter.SEARCH, что означает поиск участников на основе
#     строки запроса.

from pyrogram import enums

# Получение списка администраторов
administrators = []
async for m in app.get_chat_members(chat_id, filter=enums.ChatMembersFilter.ADMINISTRATORS):
    administrators.append(m)


# Получение списка ботов в чате
bots = []
async for m in app.get_chat_members(chat_id, filter=enums.ChatMembersFilter.BOTS):
    bots.append(m)


# Получение списка заблокированных участников (BANNED)
banned_members = []
async for member in app.get_chat_members(chat_id, filter=enums.ChatMembersFilter.BANNED):
    banned_members.append(member)


# Получение списка участников с ограничениями (RESTRICTED)
restricted_members = []
async for member in app.get_chat_members(chat_id, filter=enums.ChatMembersFilter.RESTRICTED):
    restricted_members.append(member)


# Получение списка недавно активных участников (RECENT)
recent_members = []
async for member in app.get_chat_members(chat_id, filter=enums.ChatMembersFilter.RECENT):
    recent_members.append(member)


# Поиск участников по имени или имени пользователя (SEARCH)
# Замените 'search_query' на ваш поисковый запрос
search_query = 'example'
searched_members = []
async for member in app.get_chat_members(chat_id, query=search_query, filter=enums.ChatMembersFilter.SEARCH):
    searched_members.append(member)

# 2. Получить информацию об участниках чата

def main():
    group_url = "parsinger_pyrogram"
    with app:
        members = app.get_chat_members(group_url, limit=10)
        for member in members:
            print(member.user.first_name, member.user.id)

main()




#Псевдокод для наглядного использование всех параметров
from pyrogram import Client, enums

app = Client("my_account")

def main():
    group_url = "parsinger_pyrogram"  # Имя пользователя или идентификатор чата
    query = "BigData"           # Строка поиска для фильтрации участников по имени
    limit = 10               # Максимальное количество участников для возврата
    filter1 = enums.ChatMembersFilter.SEARCH  # Фильтр для поиска по имени
    filter2 = enums.ChatMembersFilter.ADMINISTRATORS  # Фильтр для поиска администраторов чата


    with app:

        # Поиск по имени
        members = app.get_chat_members(group_url, query=query, limit=limit, filter=filter1)
        for member in members:
            print(f"Найден {member.user.first_name}, ID: {member.user.id}")

        # Поиск администраторов
        members = app.get_chat_members(group_url, limit=limit, filter=filter2)
        for member in members:
            print(f"Имя администратора: {member.user.first_name}")

if __name__ == "__main__":
    main()

# app.get_chat_member(chat_id, user_id): Получает информацию об определенном участнике чата или группы.
#
#     chat_id(int | str) - Уникальный идентификатор (int) или имя пользователя (str) целевого чата.
#
#     user_id(int | str) - Уникальный идентификатор (int) или имя пользователя (str) целевого пользователя.
#     Что касается вас самих, вы можете просто использовать me или self.
#
#     Возвращает: ChatMember– В случае успеха возвращается участник чата.

# 3. Получить информацию об участнике чата

def main():
    with app:
        group_url = "parsinger_pyrogram"     # Указываем имя группы или канала
        members = app.get_chat_member(            # Получаем информацию об участнике чата
            chat_id=group_url,                    # ID чата или его имя
            user_id='@HybridAppParser51'               # ID пользователя или его имя пользователя
        )
        print(members)                            # Выводим информацию об участнике чата

main()

# app.get_messages(chat_id, message_ids, reply_to_message_ids, replies): Используется для получения одного или
# нескольких сообщений из чата. Если message_ids не является списком, возвращается одно сообщение.
# Если message_ids является списком, возвращается список сообщений.
#
#     chat_id(int | str) - Это номер или имя чата, из которого вы хотите получить сообщения. Если вы хотите получить
#     сообщения из своих сохраненных сообщений, используйте слово "me" или "self". Для контакта, который существует в
#     вашей адресной книге Telegram, можно использовать его номер телефона (str).
#
#     message_ids(int | Iterable of int, необязательный) - Передайте идентификатор одного сообщения (int) или итерацию
#     идентификаторов сообщений (например, список int), чтобы получить содержимое этих сообщений (далее разберём
#     подробно).
#
#     reply_to_message_ids(int | Iterable of int, необязательный) - Передайте идентификатор одного сообщения или список
#     идентификаторов сообщений, чтобы получить содержимое предыдущих сообщений, на которые вы ответили этим сообщением.
#     Если установлен параметр message_ids, этот аргумент будет проигнорирован.
#
#     replies(int, необязательный) - Укажите количество последующих ответов для каждого сообщения:
#         0 — не получать ответы.
#         -1 — получить все доступные ответы (без ограничений).
#         По умолчанию: 1.

# 4. Получить сообщения из чата
def main():
    with app:
        # Получение одного сообщения по его id:
        message = app.get_messages(chat_id=group_url, message_ids=123)

        # Получение сообщения со всеми связанными ответами:
        message = app.get_messages(chat_id=group_url, message_ids=123, replies=-1)

        # Получение сообщения на которое указанное сообщение стало ответом
        #(без учета цепочки остальных ответов):
        message = app.get_messages(chat_id=group_url, reply_to_message_ids=123, replies=0)

        # Для получения нескольких конкретных сообщений:
        messages = app.get_messages(chat_id=group_url, message_ids=[123, 456, 789])

# app.search_messages(chat_id, query, offset, filter, limit, from_user): Ищет сообщения в чате или группе по
# определенным критериям.
#
#     chat_id(int | str) - Это номер или имя пользователя чата, в котором вы хотите искать сообщения. Если вы хотите
#     искать в своих сохраненных сообщениях, используйте "me" или "self".,
#
#     query(str, необязательный) - Это слово или фраза, которую вы хотите найти в сообщениях. Если вы ищете фотографии
#     или видео, этот параметр поможет найти те, у которых есть подписи с этим текстом.
#
#     offset(int, необязательный) - Это стартовая точка поиска. Если вы поставите 0, поиск начнется с самого первого
#     сообщения. Если вы поставите 10, поиск начнется с 11-го сообщения.
#
#     filter(enums.MessagesFilter, необязательный) - Это специальный фильтр, который позволяет вам искать определенные
#     типы сообщений, например, только фотографии или только видео.
#
#     limit(int, необязательный) - Это максимальное количество сообщений, которые вы хотите получить. Если вы не укажете
#     этот параметр, поиск вернет все подходящие сообщения.
#
#     from_user(int | str, необязательный) - Это номер или имя пользователя человека, чьи сообщения вы хотите найти.
#     Если вы хотите найти сообщения, которые вы отправили, используйте me или self.

#Псевдокод для демонстрации функции с параметрами

from pyrogram import Client, enums

app = Client("my_account")

def search_messages_example():
    chat_id = "Parsinger_Telethon_Test"  # ID или username чата
    query = "hello"                      # Строка для поиска в тексте сообщений
    offset = 0                           # Начинаем с первого сообщения
    filter = enums.MessagesFilter.PHOTO   # Фильтруем по сообщениям с фотографиями
    limit = 100                          # Ограничиваем количество найденных сообщений
    from_user = "some_user"              # Ищем только сообщения от пользователя "some_user"

    with app:
        for message in app.search_messages(
            chat_id=chat_id,
            query=query,
            offset=offset,
            filter=filter,
            limit=limit,
            from_user=from_user
        ):
            print(message.text)  # Вывод текста найденного сообщения

if __name__ == "__main__":
    search_messages_example()

# app.get_chat_history(chat_id, limit, offset, offset_id, offset_date): Получает историю сообщений из чата или группы.
#
#     chat_id(int | str) - Это номер или имя пользователя чата(диалога), из которого вы хотите получить сообщения. Если
#     вы хотите получить сообщения из своего личного "облака" (Saved Messages), используйте me или self.
#
#     limit(int, необязательный) - Это число, которое говорит, сколько сообщений вы хотите получить. Если вы не укажете
#     этот параметр, то по умолчанию будут возвращены все доступные сообщения.
#
#     offset(int, необязательный) - Это число, которое определяет, с какого сообщения начать подсчет. Это может быть
#     полезно, если вы хотите пропустить определенное количество сообщений в начале списка.
#
#     offset_id(int, необязательный) - Это идентификатор сообщения, с которого вы хотите начать получение сообщений.
#     Это полезно, если вы знаете конкретный ID сообщения, с которого хотите начать.
#
#     offset_date(datetime, необязательный) - Это дата, и если вы укажете ее, то будут возвращены сообщения, которые
#     были отправлены до этой даты. Это полезно, если вы хотите получить старые сообщения до определенного момента
#     времени.

# Псевдокод для демонстрации функции с параметрами

def get_history():
    with app:
        chat_id = "parsinger_pyrogram"  # Используйте ID или имя пользователя чата
        limit = 100  # Количество сообщений для получения
        offset = 0  # Смещение относительно первого сообщения в истории
        offset_id = 0  # ID сообщения, с которого начнется получение истории
        offset_date = datetime(2021, 1, 1)  # Получить сообщения, отправленные до 1 января 2021 года

        # Получаем историю чата
        for message in app.get_chat_history(chat_id, limit=limit, offset=offset, offset_id=offset_id,
                                            offset_date=offset_date):
            print(message.text)

get_history()

# app.get_chat_photos(chat_id, limit): Получает фотографии профиля чата или группы.
#
#     chat_id - Это номер или имя чата, из которого вы хотите получить фотографии. Если вы хотите свои фотографии,
#     напишите me или self. Если хотите фотографии друга, напишите его номер телефона или имя пользователя.
#     limit - Это количество фотографий, которое вы хотите получить. Если вы не скажете, сколько хотите, программа
#     попытается дать вам все фотографии.
#
#     #Псевдокод для демонстрации функции с параметрами
#
#     def main():
#         with app:
#             chat_id = "username"  # Замените на имя пользователя или ID чата
#             chat_photos = app.get_chat_photos(chat_id)
#
#             for photo in chat_photos:
#                 # Скачиваем каждую фотографию профиля
#                 app.download_media(photo.file_id, file_name=f"{photo.file_id}.jpg")
#
#
#     main()
#
#  app.download_media(photo.file_id, file_name=f"{photo.file_id}.jpg") — это метод, который скачивает фотографию
#  по её file_id и сохраняет её локально с указанным именем файла, о этом методе еще будет рассказано подробнее.


from pyrogram import Client
import asyncio

api_id = 2********2
api_hash = "8******************7"
group_url = "parsinger_pyrogram"
app = Client("my_session", api_id=api_id, api_hash=api_hash)


def main():
    with app:
        chat = app.get_chat(group_url)
        print(type(chat))

main()

# Класс pyrogram.types.user_and_chats.chat.Chat представляет собой объект чата и содержит различные атрибуты и методы
# для работы с этим чатом.
#
# Вот некоторые из атрибутов, которые могут быть доступны в объекте Chat:
#
#     chat.id: Уникальный идентификатор чата.
#     chat.type: Тип чата (может быть "private", "group", "supergroup" или "channel").
#     chat.username: Имя пользователя чата, если это личный чат, или @username канала/супергруппы.
#     chat.first_name и last_name: Имя и фамилия пользователя, если это личный чат.
#     chat.title: Название группы, супергруппы или канала.
#     chat.description: Описание группы, супергруппы или канала.
#     chat.pinned_message: Закрепленное сообщение в чате, если оно есть.
#     chat.permissions: Права участников чата.
#     chat.photo: Фотография профиля чата, если она установлена.

# Этот JSON представляет собой словарь с информацией о чате в Telegram, полученной с использованием библиотеки
# Pyrogram. Вот описание каждой строки:
#
# Для лучше читаемости, скопируйте этот JSON куда-нибудь где нет ограничений по длине строки.

{
    "_": "Chat",                            # Тип объекта, в данном случае это чат.
    "id": -1001795821154,                   # Уникальный идентификатор чата. (chat.id)
    "type": "ChatType.SUPERGROUP",          # Тип чата, в данном случае это супергруппа. (chat.type)
    "is_verified": false,                   # Флаг, показывающий, верифицирован ли чат. (chat.is_verified)
    "is_restricted": false,                 # Флаг, показывающий, ограничен ли доступ к чату. (chat.is_restricted)
    "is_creator": false,                    # Флаг, показывающий, является ли пользователь создателем чата. (chat.is_creator)
    "is_scam": false,                       # Флаг, показывающий, является ли чат мошенническим. (chat.is_scam)
    "is_fake": false,                       # Флаг, показывающий, является ли чат фальшивым. (chat.is_fake)
    "title": "Parsinger_Telethon_Test",     # Название чата. (chat.title)
    "username": "Parsinger_Telethon_Test",  # Имя пользователя чата (если это канал или супергруппа). (chat.username)
    "photo": {                              # Фотография профиля чата. (chat.photo)
        "_": "ChatPhoto",                   # Тип объекта, в данном случае это фотография чата.
        "small_file_id": "AQADAgAD7MMxG4XoQUoAEAIAA57hUMAW____Ft-3784XVesABB4E",  # ID маленькой версии фотографии. (chat.photo.small_file_id)
        "small_photo_unique_id": "AgAD7MMxG4XoQUo",                               # Уникальный ID маленькой версии фотографии. (chat.photo.small_photo_unique_id)
        "big_file_id": "AQADAgAD7MMxG4XoQUoAEAMAA57hUMAW____Ft-3784XVesABB4E",    # ID большой версии фотографии. (chat.photo.big_file_id)
        "big_photo_unique_id": "AgAD7MMxG4XoQUo"                                  # Уникальный ID большой версии фотографии. (chat.photo.big_photo_unique_id)
    },
    "description": "dgf8974503g+3804553g4+556034+5j08456670k4865;740359-'4=0654544066f5450646554k0456678064+g466445+97460h4567321645k565789060k67584890546673574560+7tg456857+45680g766409j328740658974=-60954=564365405426531405g325464562503d4535424365067h74563765j5646857k40063",  # Описание чата. (chat.description)
    "dc_id": 2,                             # ID центра данных, где хранится информация о чате. (chat.dc_id)
    "has_protected_content": false,         # Флаг, показывающий, содержит ли чат защищенный контент. (chat.has_protected_content)
    "pinned_message": {                     # Закрепленное сообщение в чате. (chat.pinned_message)
        "_": "Message",                     # Тип объекта, в данном случае это сообщение.
        "id": 330,                          # ID сообщения. (chat.pinned_message.id)
        "from_user": {                      # Пользователь, отправивший сообщение. (chat.pinned_message.from_user)
            "_": "User",                    # Тип объекта, в данном случае это пользователь.
            "id": 5799846345,               # ID пользователя. (chat.pinned_message.from_user.id)
            "is_self": false,               # Флаг, показывающий, является ли пользователь текущим пользователем. (chat.pinned_message.from_user.is_self)
            "is_contact": false,            # Флаг, показывающий, находится ли пользователь в контактах. (chat.pinned_message.from_user.is_contact)
            "is_mutual_contact": false,     # Флаг, показывающий, является ли пользователь взаимным контактом. (chat.pinned_message.from_user.is_mutual_contact)
            "is_deleted": false,            # Флаг, показывающий, удален ли аккаунт пользователя. (chat.pinned_message.from_user.is_deleted)
            "is_bot": false,                # Флаг, показывающий, является ли пользователь ботом. (chat.pinned_message.from_user.is_bot)
            "is_verified": false,           # Флаг, показывающий, верифицирован ли пользователь. (chat.pinned_message.from_user.is_verified)
            "is_restricted": false,         # Флаг, показывающий, ограничен ли доступ пользователя. (chat.pinned_message.from_user.is_restricted)
            "is_scam": false,               # Флаг, показывающий, является ли аккаунт пользователя мошенническим. (chat.pinned_message.from_user.is_scam)
            "is_fake": false,               # Флаг, показывающий, является ли аккаунт пользователя фальшивым. (chat.pinned_message.from_user.is_fake)
            "is_support": false,            # Флаг, показывающий, является ли пользователь сотрудником поддержки Telegram. (chat.pinned_message.from_user.is_support)
            "is_premium": false,            # Флаг, показывающий, является ли пользователь премиум-пользователем. (chat.pinned_message.from_user.is_premium)
            "first_name": "Larry",          # Имя пользователя. (chat.pinned_message.from_user.first_name)
            "last_name": "Summers",         # Фамилия пользователя. (chat.pinned_message.from_user.last_name)
            "status": "UserStatus.OFFLINE",             # Статус пользователя (в данном случае оффлайн). (chat.pinned_message.from_user.status)
            "last_online_date": "2023-01-24 15:39:57",  # Последняя дата онлайн. (chat.pinned_message.from_user.last_online_date)
            "username": "Larry_Summers",                # Имя пользователя в Telegram. (chat.pinned_message.from_user.username)
            "dc_id": 5,                                 # ID центра данных, где хранится информация о пользователе. (chat.pinned_message.from_user.dc_id)
            "photo": {                                  # Фотография профиля пользователя. (chat.pinned_message.from_user.photo)
                "_": "ChatPhoto",                       # Тип объекта, в данном случае это фотография чата.
                "small_file_id": "AQADBQADAbExGw3rgFYAEAIAA8mhslkBAAPoL1uFHxdshgAEHgQ",  # ID маленькой версии фотографии. (chat.pinned_message.from_user.photo.small_file_id)
                "small_photo_unique_id": "AgADAGw3rgFY",                                 # Уникальный ID маленькой версии фотографии. (chat.pinned_message.from_user.photo.small_photo_unique_id)
                "big_file_id": "AQADBQADAbExGw3rgFYAEAMAA8mhslkBAAPoL1uFHxdshgAEHgQ",    # ID большой версии фотографии. (chat.pinned_message.from_user.photo.big_file_id)
                "big_photo_unique_id": "AgADAb3rgFY"                                     # Уникальный ID большой версии фотографии. (chat.pinned_message.from_user.photo.big_photo_unique_id)
            }
        },
        "date": "2023-01-24 15:27:03",          # Дата отправки сообщения. (chat.pinned_message.date)
        "chat": {                               # Чат, в котором было отправлено сообщение. (chat.pinned_message.chat)
                                                # ... (информация о чате, аналогична предыдущему описанию)
        },
        "mentioned": false,                     # Флаг, показывающий, упоминается ли в сообщении текущий пользователь. (chat.pinned_message.mentioned)
        "scheduled": false,                     # Флаг, показывающий, является ли сообщение запланированным. (chat.pinned_message.scheduled)
        "from_scheduled": false,                # Флаг, показывающий, отправлено ли сообщение из запланированных. (chat.pinned_message.from_scheduled)
        "media": "MessageMediaType.PHOTO",      # Тип медиа в сообщении (в данном случае фото). (chat.pinned_message.media)
        "has_protected_content": false,         # Флаг, показывающий, содержит ли сообщение защищенный контент. (chat.pinned_message.has_protected_content)
        "has_media_spoiler": false,             # Флаг, показывающий, содержит ли сообщение спойлер медиа. (chat.pinned_message.has_media_spoiler)
        "photo": {
            "_": "Photo",                       # Тип объекта
            "file_id": "AgACAgUAAx0CawoOYgACAUplQ1g5FZecjTHSMcKeyBXYOqQiEQACdLUxGztEeVb1sKmzMscIDgAIAQADAgADeAAHHgQ",  # ID файла фотографии (chat.pinned_message.photo.file_id)
            "file_unique_id": "AgADdLUxGztEeVY",    # Уникальный ID файла фотографии (chat.pinned_message.photo.file_unique_id)
            "width": 700,                           # Ширина фотографии (chat.pinned_message.photo.width)
            "height": 700,                          # Высота фотографии (chat.pinned_message.photo.height)
            "file_size": 72267,                     # Размер файла фотографии в байтах (chat.pinned_message.photo.file_size)
            "date": "2023-01-24 15:27:02",          # Дата отправки фотографии (chat.pinned_message.photo.date)
            "thumbs": [                             # Миниатюры фотографии (chat.pinned_message.photo.thumbs)
                {
                    "_": "Thumbnail",               # Тип объекта
                    "file_id": "AgACAgUAAx0CawoOYgACAUplQ1g5FZecjTHSMcKeyBXYOqQiEQACdLUxGztEeVb1sKmzMscIDgAIAQADAgADbQAHHgQ",  # ID файла миниатюры (chat.pinned_message.photo.thumbs[0].file_id)
                    "file_unique_id": "AgADdLUxGztEeVY",    # Уникальный ID файла миниатюры (chat.pinned_message.photo.thumbs[0].file_unique_id)
                    "width": 320,                           # Ширина миниатюры (chat.pinned_message.photo.thumbs[0].width)
                    "height": 320,                          # Высота миниатюры (chat.pinned_message.photo.thumbs[0].height)
                    "file_size": 25406                      # Размер файла миниатюры в байтах (chat.pinned_message.photo.thumbs[0].file_size)
                }
            ]
        },
        "outgoing": false,  # Флаг, показывающий, является ли сообщение исходящим (chat.pinned_message.outgoing)
        "can_set_sticker_set": false,  # Флаг, показывающий, может ли пользователь устанавливать набор стикеров в чате (chat.can_set_sticker_set)
        "members_count": 20,  # Количество участников чата (chat.members_count)
        "permissions": {  # Права участников чата (chat.permissions)
            "_": "ChatPermissions",  # Тип объекта
            "can_send_messages": false,  # Флаг, показывающий, могут ли участники отправлять сообщения (chat.permissions.can_send_messages)
            "can_send_media_messages": false,  # Флаг, показывающий, могут ли участники отправлять медиа-сообщения (chat.permissions.can_send_media_messages)
            "can_send_other_messages": false,  # Флаг, показывающий, могут ли участники отправлять другие типы сообщений (chat.permissions.can_send_other_messages)
            "can_send_polls": false,  # Флаг, показывающий, могут ли участники отправлять опросы (chat.permissions.can_send_polls)
            "can_add_web_page_previews": false,  # Флаг, показывающий, могут ли участники добавлять предпросмотр веб-страниц (chat.permissions.can_add_web_page_previews)
            "can_change_info": false,  # Флаг, показывающий, могут ли участники изменять информацию о чате (chat.permissions.can_change_info)
            "can_invite_users": false,  # Флаг, показывающий, могут ли участники приглашать других пользователей (chat.permissions.can_invite_users)
            "can_pin_messages": false  # Флаг, показывающий, могут ли участники закреплять сообщения (chat.permissions.can_pin_messages)
        }
}


chat.pinned_message.from_user.photo.big_photo_unique_id

# Этот путь обращается к следующим элементам в этой структуре данных:
#
#     chat: Объект чата.
#     pinned_message: Закрепленное сообщение в чате.
#     from_user: Пользователь, отправивший закрепленное сообщение.
#     photo: Фотография профиля пользователя.
#     big_photo_unique_id: Уникальный идентификатор большой версии фотографии профиля пользователя.
#
# Точка (.) в выражении chat.pinned_message.from_user.photo.big_photo_unique_id используется для доступа к атрибутам или
# свойствам объекта. Это называется "точечная нотация". Каждая точка в выражении указывает на переход к вложенному
# атрибуту или свойству объекта. Таким образом можно извлекать любые данные из любых объектов предоставляемые API
# Telegram.