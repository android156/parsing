from pyrogram import Client, filters
import asyncio

# Укажите свои API ID и API Hash для подключения к Telegram API
api_id = 2*******2
api_hash = "8****************7"

# Создание клиента Pyrogram для взаимодействия с Telegram
app = Client("my_session", api_id=api_id, api_hash=api_hash)

# Список чатов, в которых будет производиться поиск сообщений
chats = ['ru_python', 'python_scripts', 'moscowpythonconf', 'rudepython', 'pythonchatru',
         'python_academy_chat', 'python_noobs', 'pythontalk_chat', 'pythonguruchat',
         'Python', 'pydjango', 'ChatPython', 'ru_python_beginners', 'karpovcourseschat']

# Список ключевых слов для поиска в сообщениях
words = ['.', ',']

# Функция для проверки сообщений на наличие ключевых слов
async def check_message(client, message):
    print(f"Новое сообщение из {message.chat.title}: {message.text}")  # Вывод каждого нового сообщения в консоль
    for word in words:
        if word in message.text:
            chat_link = f"https://t.me/{message.chat.username}" if message.chat.username else "Приватный чат"
            sender = f"@{message.from_user.username}" if message.from_user.username else "Неизвестный отправитель"

            text = f"Чат: {chat_link}\nНайдена фраза: {word}\nОтправитель: {sender}\nСообщение полностью: {message.text}"
            print(text)

            # Замените '@username' на имя вашего чата или вашего пользователя для получения уведомлений
            await client.send_message('@username', text)

            await asyncio.sleep(5)  # Задержка перед отправкой реакции
            # await client.send_reaction(message.chat.id, message.id, "👍")


@app.on_message(filters.chat(chats) & filters.text)
async def message_handler(client, message):
    await check_message(client, message)


# Запускаем клиента Pyrogram
app.run()