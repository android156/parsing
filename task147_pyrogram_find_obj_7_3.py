import asyncio
import pprint
import json

from pyrogram import Client, enums

api_id = 25300378
api_hash = "b1d1f4c93bf8f885a884030878eaa9bc"
group_url = "parsinger_pyrogram"


# 1. Получить информацию о чате

async def main():
    app = Client("my_session", api_id=api_id, api_hash=api_hash)
    async with app:
        chat = await app.get_chat(group_url)
        chat_id = chat.id
        print('Информация о чате:')
        print(chat)
        print("Chat ID:", chat_id)
        print("Chat pinned message:", chat.pinned_message)
        print('/n/n')
        pprint.pprint(vars(chat))
        messages = app.search_messages(
            chat_id=chat_id,
            limit=20,
            filter=enums.MessagesFilter.PINNED,
            # from_user='parsinger_pyrogram'
        )
        photo_messages = []
        async for message in messages:
            print('*' * 100)
            if message.photo:
                print('Закрепленное сообщение с фото:')
                print(message)
                photo_messages.append(message)
            else:
                print("В этом прикрепленном сообщении нет фото:")
                print('ID message:', message.id)
        print(len(photo_messages))


asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
if __name__ == "__main__":
    asyncio.run(main())
