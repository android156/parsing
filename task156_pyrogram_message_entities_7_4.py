from pyrogram import Client
from pyrogram.enums import MessagesFilter

api_id = 25300378
api_hash = "b1d1f4c93bf8f885a884030878eaa9bc"

app = Client("my_session", api_id=api_id, api_hash=api_hash)


def main():
    with app:
        group_url = "parsinger_pyrogram"
        messages = app.get_chat_history(group_url)  # Получаем историю чата для указанной группы
        for message in messages:  # Перебираем все сообщения в истории чата
            if message.entities:  # Проверяем, есть ли у сообщения сущности (например, ссылки)
                for entity in message.entities:  # Перебираем все сущности в сообщении

                    entity_type = entity.type

                    print(f"Найдена сущность: {entity_type}\n")  # Отладочное сообщение
                    print('==>', message.text)
                    print('------------------------------\n')

                    if entity.url:  # Проверяем, содержит ли сущность URL
                        print('Отдельная проверка на url: ' ,entity.url)


main()

#
#
#     MessageEntityType.MENTION: Упоминание пользователя с @username
#     MessageEntityType.HASHTAG: Хештег с #hashtag
#     MessageEntityType.CASHTAG: Кэштег с $USD
#     MessageEntityType.BOT_COMMAND: Команда бота, например /start@pyrogrambot
#     MessageEntityType.URL: URL-адреса, например https://pyrogram.org
#     MessageEntityType.EMAIL: Электронная почта, например do-not-reply@pyrogram.org
#     MessageEntityType.PHONE_NUMBER: Номер телефона, например +1-123-456-7890
#     MessageEntityType.BOLD: Жирный текст
#     MessageEntityType.ITALIC: Курсивный текст
#     MessageEntityType.UNDERLINE: Подчеркнутый текст
#     MessageEntityType.STRIKETHROUGH: Текст с зачеркиванием
#     MessageEntityType.SPOILER: Текст спойлера
#     MessageEntityType.CODE: Строка моноширинного шрифта
#     MessageEntityType.PRE: Блок моноширинного шрифта (с указанием языка)
#     MessageEntityType.BLOCKQUOTE: Текст цитаты
#     MessageEntityType.TEXT_LINK: Для кликабельных текстовых URL
#     MessageEntityType.TEXT_MENTION: Для упоминания пользователей без имени пользователя (с указанием пользователя)
#     MessageEntityType.BANK_CARD: Текст банковской карты
#     MessageEntityType.CUSTOM_EMOJI: Пользовательские эмодзи
#     MessageEntityType.UNKNOWN: Неизвестный тип сущности сообщения

#
