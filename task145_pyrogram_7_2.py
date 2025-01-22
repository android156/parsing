from pyrogram import Client

api_id = 25300378
api_hash = "b1d1f4c93bf8f885a884030878eaa9bc"
group_url = "python_parsing"
app = Client("my_session", api_id=api_id, api_hash=api_hash)


def main():
    with app:
        all_messages = []
        for message in app.get_chat_history(group_url, limit=100):
            all_messages.append(message.text)

        # Вывод сообщений на экран или сохранение в файл
        for msg in all_messages:
            print(msg)


main()