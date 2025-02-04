import asyncio
import random

from pyrogram import Client, filters

from env import API_ID, API_HASH

app = Client("my_first_session", api_id=API_ID, api_hash=API_HASH)

chats = []
emojis = ['💩', '🤡']


async def check_message(client, message):
    print(message.from_user.id, message.text)
    if message.from_user.is_self:
        return
    await asyncio.sleep(random.randint(3, 6))
    await client.send_reaction(message.chat.id, message.id, random.choice(emojis))


@app.on_message(filters.chat(chats))
async def message_handler(client, message):
    await check_message(client, message)


app.run()
