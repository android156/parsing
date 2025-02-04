#
# app.get_users(user_ids) - Метод позволяет получить информацию о пользователях по их идентификаторам или именам пользователей. Он возвращает детальную информацию о профиле, включая имя, фамилию, фотографии профиля и другие данные.
# Пример использования: app.get_users(user_ids)
#
def main():
    with app:
        user_ids = [6559275957, 6833360952]
        users = app.get_users(user_ids)
        for user in users:
            print(user.id, user.first_name)
#
# Вывод:
#
# 6559275957 Db
# 6833360952 Angular
#
#
#
# get_chat:
# Хотя этот метод в основном используется для получения информации о чатах, он также может быть использован для получения информации о профилях пользователей, если указать идентификатор пользователя в качестве параметра.
# Пример использования: app.get_chat(user_id)
#
# get_chat_photos:
# Этот метод используется для последовательного получения фотографий профиля чата или пользователя. Он возвращает генератор отдающий объекты Photo.
# Пример использования:
#
async for photo in app.get_chat_photos("me"):
    print(photo)
#
#
#
# get_contacts:
# Если пользователь разрешил доступ к своим контактам, этот метод позволяет получить список контактов пользователя.
# Пример использования: app.get_contacts()

from pyrogram import Client

api_id = 2**********2
api_hash = "8******************7"
app = Client("my_session", api_id=api_id, api_hash=api_hash)


def main():
    with app:
        user_chat = app.get_users(6833360952)
        print(user_chat)

main()

{
    "_": "User",  # Тип объекта, в данном случае это 'User'
    "id": 6833360952,  # Уникальный идентификатор пользователя в Telegram
    "is_self": false,  # Показывает, является ли этот пользователь текущим пользователем бота/клиента
    "is_contact": false,  # Указывает, находится ли этот пользователь в контактах текущего пользователя
    "is_mutual_contact": false,  # Показывает, является ли контакт взаимным
    "is_deleted": false,  # Указывает, удален ли аккаунт пользователя
    "is_bot": false,  # Показывает, является ли этот пользователь ботом
    "is_verified": false,  # Указывает, верифицирован ли аккаунт пользователя (официальный аккаунт)
    "is_restricted": false,  # Показывает, ограничен ли аккаунт пользователя (например, за нарушение правил Telegram)
    "is_scam": false,  # Указывает, помечен ли аккаунт как мошеннический
    "is_fake": false,  # Показывает, является ли аккаунт фальшивым
    "is_support": false,  # Указывает, является ли пользователь сотрудником поддержки Telegram
    "is_premium": false,  # Показывает, использует ли пользователь премиум-версию Telegram
    "first_name": "Angular",  # Имя пользователя
    "last_name": "Expert",  # Фамилия пользователя
    "status": "UserStatus.OFFLINE",  # Статус пользователя (в данном случае оффлайн)
    "last_online_date": "2023-11-08 11:35:07",  # Последняя дата и время, когда пользователь был онлайн
    "username": "AngularExpert44",  # Имя пользователя в Telegram (username)
    "dc_id": 5,  # Идентификатор центра данных, к которому подключен пользователь
    "photo": {  # Информация о фотографии профиля пользователя
        "_": "ChatPhoto",  # Тип объекта фотографии, в данном случае 'ChatPhoto'
        "small_file_id": "AQADBQADqrgxG-0gYFYAEAIAAzjQTJcBAAMjVwuGQ3qpWAAEHgQ",
        # Идентификатор маленькой версии фотографии
        "small_photo_unique_id": "AgADqrgxG-0gYFY",  # Уникальный идентификатор маленькой версии фотографии
        "big_file_id": "AQADBQADqrgxG-0gYFYAEAMAAzjQTJcBAAMjVwuGQ3qpWAAEHgQ",  # Идентификатор большой версии фотографии
        "big_photo_unique_id": "AgADqrgxG-0gYFY"  # Уникальный идентификатор большой версии фотографии
    }
}

# Доступ к основным полям объекта User
user_id = user.id                       # ID пользователя
first_name = user.first_name            # Имя пользователя
last_name = user.last_name              # Фамилия пользователя, может быть None
username = user.username                # Имя пользователя (username), может быть None
is_bot = user.is_bot                    # Проверка, является ли пользователь ботом
is_verified = user.is_verified          # Проверка, верифицирован ли пользователь
status = user.status                    # Статус пользователя (например, 'offline', 'online')

# Доступ к фотографиям профиля, если установлены
if user.photo:
    small_photo_id = user.photo.small_file_id   # ID маленькой фотографии профиля
    big_photo_id = user.photo.big_file_id       # ID большой фотографии профиля


#-----------------#
User ID: 6833360952
Name: Angular Expert
Username: @AngularExpert44
Bot: No
Verified: No
Status: UserStatus.OFFLINE
Small Photo ID: AQADBQADqrgxG-0gYFYAEAIAAzjQTJcBAAMjVwuGQ3qpWAAEHgQ
Big Photo ID: AQADBQADqrgxG-0gYFYAEAMAAzjQTJcBAAMjVwuGQ3qpWAAEHgQ


from pyrogram import Client
from pyrogram.errors import PeerIdInvalid

app = Client("session_nawme5")
group_url = "parsinger_pyrogram"

id_list = [332703068, 6722388543, 6520262354, 6417114754, 6559275957, 6833360952,
           6362909579, 6864407564, 6948347806, 6872035583, 6706079415, 6971022916,
           6520728024, 6734487015, 6375028301, 6607414815, 6831043726, 6831043762]

def main():
    with app:
        # Итерируемся по списку, выводя актуальную информацию профиля каждого участника
        for user_id in id_list:
            try:
                user_chat = app.get_users(user_id)
                print(user_chat)
            except PeerIdInvalid:
                print(f"Ошибка: Неправильный идентификатор {user_id}.")

main()