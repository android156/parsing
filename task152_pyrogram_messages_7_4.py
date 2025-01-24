import asyncio
import pprint
import json

import pyrogram
from pyrogram import Client, enums

api_id = 25300378
api_hash = "b1d1f4c93bf8f885a884030878eaa9bc"
group_url = "parsinger_pyrogram"

app = Client("my_session", api_id=api_id, api_hash=api_hash)


# Получаем историю чата
def main():
    with app:
        sum = 0
        messages = app.get_chat_history(group_url)
        for message in messages:
            if message.text and message.text.isdecimal():
               sum += int(message.text)
            print(f'message text: {message.text}')
        print(sum)


main()
