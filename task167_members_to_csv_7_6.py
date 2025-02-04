from pyrogram import Client
import csv

api_id = 2*******2
api_hash = "8*****************7"
app = Client("my_session", api_id=api_id, api_hash=api_hash)
group_url = "parsinger_pyrogram" 

def main():
    with app:
        with open("members.csv", "w", newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            # Добавляем новые заголовки столбцов
            writer.writerow(["ID", "Username", "First Name", "Last Name", "Phone Number",
                             "Last Online Date", "Joined Date", "Is Bot", "Is Self",
                             "Is Contact", "Is Verified", "Is Restricted", "Is Scam",
                             "Is Fake", "Is Support", "Is Premium"])

            for member in app.get_chat_members(group_url):
                user = member.user

                # Получаем дополнительные поля
                user_id = user.id
                username = f"@{user.username}" if user.username else "None"
                first_name = user.first_name if user.first_name else "None"
                last_name = user.last_name if user.last_name else "None"
                phone_number = user.phone_number if user.phone_number else "None"
                last_online_date = user.last_online_date if user.last_online_date else "None"
                joined_date = member.joined_date if hasattr(member, 'joined_date') else "None"
                is_bot = user.is_bot

                # Дополнительные поля из объекта user
                is_self = user.is_self
                is_contact = user.is_contact
                is_verified = user.is_verified
                is_restricted = user.is_restricted
                is_scam = user.is_scam
                is_fake = user.is_fake
                is_support = user.is_support
                is_premium = user.is_premium

                # Дополненная запись данных пользователя в CSV
                writer.writerow([user_id, username, first_name, last_name, phone_number,
                                 last_online_date, joined_date, is_bot, is_self, is_contact,
                                 is_verified, is_restricted, is_scam, is_fake, is_support,
                                 is_premium])

                # Опциональный вывод информации
                print(f"ID: {user_id}, Username: {username}, First Name: {first_name}, Last Name: {last_name}, Phone Number: {phone_number}, Last Online: {last_online_date}, Joined Date: {joined_date}, Is Bot: {is_bot}, Is Self: {is_self}, Is Contact: {is_contact}, Is Verified: {is_verified}, Is Restricted: {is_restricted}, Is Scam: {is_scam}, Is Fake: {is_fake}, Is Support: {is_support}, Is Premium: {is_premium}")
                print('-------------')

main()