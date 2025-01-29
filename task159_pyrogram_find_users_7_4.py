from pyrogram import Client
from pyrogram.enums import MessagesFilter
import asyncio

api_id = 25300378
api_hash = "b1d1f4c93bf8f885a884030878eaa9bc"

lock = asyncio.Lock()

async def main():
    app = Client("my_session", api_id=api_id, api_hash=api_hash)
    chat_name = 'parsinger_pyrogram'  # Например, можно использовать @username для публичных каналов или чатов
    async with app:
        chat = await app.get_chat(chat_name)
        chat_id = chat.id
        print('Информация о чате:')
        print(type(chat))
        print(chat.title)
        print("Chat ID:", chat_id)
        print('\n\n')
        last_online_date = None
        last_online_user_id = None
        async for member in chat.get_members():
            print(member.user.id, member.user.username, member.user.last_online_date)
            async with lock:
                if not last_online_date or member.user.last_online_date < last_online_date:
                    last_online_date = member.user.last_online_date
                    last_online_user_id = member.user.id



        print(last_online_date, last_online_user_id)

asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
if __name__ == "__main__":
    asyncio.run(main())