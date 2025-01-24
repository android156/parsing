import asyncio
import pprint
import json

import pyrogram
from pyrogram import Client, enums

api_id = 25300378
api_hash = "b1d1f4c93bf8f885a884030878eaa9bc"
group_url = "python_parsing"

app = Client("my_session", api_id=api_id, api_hash=api_hash)


# Получаем историю чата
def main():
    with app:
        messages = app.get_chat_history(group_url, limit=10)
        for message in messages:
            print('*' * 50)
            print(f'ID: {message.id}')
            print(f'from_user ID: {message.from_user.id}')
            print(f'from_user first_name: {message.from_user.first_name}')
            print(f'from_user username: {message.from_user.username}')
            print(f'message chat ID: {message.chat.id}')
            print(f'message chat type: {message.chat.type}')
            print(f'message chat title: {message.chat.title}')
            print(f'message chat user: {message.chat.username}')
            print(f'message text: {message.text}')
            print(f'reply message ID: {message.reply_to_message_id}')


main()
