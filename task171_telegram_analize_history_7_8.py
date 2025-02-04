import asyncio
import json
from pyrogram import Client


api_id = 2**********2
api_hash = "8*****************7"


chats = ['ru_python', 'python_scripts', 'moscowpythonconf', 'rudepython', 'pythonchatru',
         'python_academy_chat', 'python_noobs', 'pythontalk_chat', 'pythonguruchat',
         'Python', 'pydjango', 'ChatPython', 'ru_python_beginners', 'karpovcourseschat']
words = ['курс']


async def contains_keywords(message, keywords):
    """
    Возвращает словарь, где ключи - это слова, а значения - True или False
    в зависимости от того, найдено ли слово в сообщении.
    Если сообщение отсутствует, возвращает словарь с False для всех слов.
    """
    if message:
        return {word: word in message.lower() for word in keywords}
    return {word: False for word in keywords}


async def save_to_file(data, file, lock):
    """Асинхронная функция для сохранения данных в формате JSON"""
    async with lock:  # Ограничение на доступ к файлу
        json.dump(data, file, ensure_ascii=False, indent=4)
        file.write("\n")  # Разделяем записи новой строкой для удобства
    print("Сообщение сохранено в файл:", data)


def create_message_link(chat, message_id):
    """Асинхронная функция для создания ссылки на сообщение"""
    return f"https://t.me/{chat}/{message_id}"


# Основная асинхронная функция для работы со скриптом
async def process_chat(app, chat, semaphore, file, lock):
    async with semaphore:  # Ограничиваем количество одновременных задач
        print(f"Проверка чата: {chat}")
        async for message in app.get_chat_history(chat, limit=100):
            keywords_found = await contains_keywords(message.text, words)
            if message.text and any(keywords_found.values()):
                message_link = create_message_link(chat, message.id)
                data = {
                    "Чат": chat,
                    "Найдена фраза": keywords_found,
                    "Отправитель": f"@{message.from_user.username}" if message.from_user else "Неизвестно",
                    "Дата отправки": str(message.date),
                    "Сообщение полностью": message.text,
                    "Ссылка на сообщение": message_link,
                }
                # Сохранение данных в файл
                await save_to_file(data, file, lock)

        print(f"Завершена обработка чата '{chat}'")


# Основная асинхронная функция для работы со скриптом
async def main():
    # Инициализация асинхронного клиента Pyrogram
    async with Client("my_session", api_id=api_id, api_hash=api_hash) as app:
        semaphore = asyncio.Semaphore(3)  # Ограничение на 3 одновременные задачи
        lock = asyncio.Lock()  # Блокировка для синхронизации записи в файл
        with open('saved_messages.txt', 'w', encoding='utf-8') as file:  # Открываем файл один раз
            # Создание списка задач
            tasks = [process_chat(app, chat, semaphore, file, lock) for chat in chats]
            # Запуск задач на конкурентное выполнение и ожидание их завершения
            await asyncio.gather(*tasks)


asyncio.run(main())