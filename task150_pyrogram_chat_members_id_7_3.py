import asyncio
import pprint
import json

import pyrogram
from pyrogram import Client, enums

api_id = 25300378
api_hash = "b1d1f4c93bf8f885a884030878eaa9bc"
group_url = "parsinger_pyrogram"


def rec_get_value(key, my_dict, path="\\"):

    if key in my_dict:
        print(f'''
        {'*' * 100}
        Ключ {key} найден. Значение {my_dict[key]}
        {'*' * 100}        
        ''')
        return my_dict[key]

    print(f'В {path} не найдено')
    for k, v in my_dict.items():
        if isinstance(v, dict):
            current_path = f"{path}{k}"  # Обновляем текущий путь
            print(f"Проверяем путь: {current_path}")
            result = rec_get_value(key, v, current_path + "\\")
            if result:
                return result
    return None


def is_pyrogram_object(obj: object) -> bool:
    """
    Проверяет, является ли объект объектом Pyrogram.
    """
    return obj.__class__.__module__.startswith("pyrogram.")


def object_to_dict(obj, seen=None):
    """
    Рекурсивно преобразует объекты Pyrogram и их атрибуты в словари, избегая циклических ссылок.
    """
    if seen is None:
        seen = set()

    if isinstance(obj, (str, int, float, bool, type(None))):
        return obj  # Простые типы данных остаются неизменными
    elif isinstance(obj, dict):
        return {key: object_to_dict(value, seen) for key, value in obj.items()}  # Обрабатываем словарь
    elif isinstance(obj, list):
        return [object_to_dict(item, seen) for item in obj]  # Обрабатываем список
    elif isinstance(obj, tuple):
        return tuple(object_to_dict(item, seen) for item in obj)  # Обрабатываем кортеж
    elif is_pyrogram_object(obj):
        obj_id = id(obj)
        if obj_id in seen:  # Проверяем, был ли объект уже обработан
            return f"<Circular reference to {type(obj).__name__} at {obj_id}>"
        seen.add(obj_id)
        return {key: object_to_dict(value, seen) for key, value in vars(obj).items()}  # Преобразуем объект Pyrogram
    else:
        return str(obj)  # Для объектов неизвестных типов возвращаем строковое представление




# 1. Получить информацию о чате

async def main():
    app = Client("my_session", api_id=api_id, api_hash=api_hash)
    async with app:
        chat = await app.get_chat(group_url)
        chat_id = chat.id
        print('Информация о чате:')
        print(type(chat))
        print(chat.get_members())
        print("Chat ID:", chat_id)
        # print("Chat pinned message:", chat.pinned_message)
        print('\n\n')
        sum = 0
        async for member in chat.get_members():
            print(member.user.id, member.user.username,)
            sum += int(member.user.id)
        print(sum)
        # chat_dict = object_to_dict(chat)
        # pprint.pprint(chat_dict)

        # print(rec_get_value("big_photo_unique_id", chat_dict))

        # messages = app.search_messages(
        #     chat_id=chat_id,
        #     limit=20,
        #     filter=enums.MessagesFilter.PINNED,
        #     # from_user='parsinger_pyrogram'
        # )
        # photo_messages = []
        # async for message in messages:
        #     print('*' * 100)
        #     if message.photo:
        #         print('Закрепленное сообщение с фото:')
        #         print(message)
        #         photo_messages.append(message)
        #     else:
        #         print("В этом прикрепленном сообщении нет фото:")
        #         print('ID message:', message.id)
        # print(len(photo_messages))


asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
if __name__ == "__main__":
    asyncio.run(main())
