import datetime
from api_info import API_ID, API_HASH
from telethon import TelegramClient, events, sync, connection
from telethon.tl.functions.users import GetFullUserRequest
import asyncio
import pyperclip
import os

url = 'https://t.me/Parsinger_Telethon_Test'

lst = [7478070952, 6388067367, 6903264582,
       6508314190, 6785254031, 6774119671,
       6807753588, 6496620987, 6788724315,
       6810623013, 6816260703, 6581321535]


sum = 0
with TelegramClient('session_name2', API_ID, API_HASH, system_version="5.10.7 beta x64") as client:
    participants = client.iter_participants(url)

    # print('participants =', participants)
    for user in participants:
        user_full = client(GetFullUserRequest(user))
        if user_full.full_user.about:
            about = user_full.full_user.about
            print(about)
            if int(user.id) in lst:
                sum += int(about)


print(sum)

# UserFull(
#
#     user=User(
#         id=2********2,
#         is_self=True,
#         contact=True,
#         mutual_contact=True,
#         deleted=False,
#         bot=False,
#         bot_chat_history=False,
#         bot_nochats=False,
#         verified=False,
#         restricted=False,
#         min=False,
#         bot_inline_geo=False,
#         support=False,
#         scam=False,
#         apply_min_photo=True,
#         fake=False,
#         access_hash=32**************2,
#         first_name='Павел',
#         last_name=Хошев,
#         username='Pashikk',
#         phone=+7 *** 5** 5* 0* ,
#     photo=UserProfilePhoto(
#         photo_id=9*************5,
#         dc_id=2,
#         has_video=False,
#         stripped_thumb=b'\****\x08\x0b\xedA!9\xcf~\xd4QE+\xb1(\xa7\xd0'),
#         status=UserStatusRecently(),
#         bot_info_version=None,
#         restriction_reason=[],
#         bot_inline_placeholder=None,
#         lang_code=None),
#     settings=PeerSettings(
#         report_spam=False,
#         add_contact=False,
#         block_contact=False,
#         share_contact=False,
#         need_contacts_exception=True,
#         report_geo=False,
#         autoarchived=False,
#         invite_members=False,
#         geo_distance=None),
#     notify_settings=PeerNotifySettings(
#         show_previews=None,
#         silent=None,
#         mute_until=None,
#         sound=None),
#     common_chats_count=3,
#     blocked=False,
#     phone_calls_available=True,
#     phone_calls_private=False,
#     can_pin_message=True,
#     has_scheduled=False,
#     video_calls_available=True,
#     about='Описание профиля',
#     profile_photo=Photo(
#         id=9**************5,
#         access_hash=5***********48,
#         file_reference=b'\x00b\xa4\xea\xf3w&ji\xd0|\xf4\x10\xdc+\xfe\\<`\x1d\xbe',

# from telethon import TelegramClient
# import asyncio
# from telethon.tl.functions.users import GetFullUserRequest
#
# api_id =
# api_hash =
# group =
#
#
# async def main():
#     async with TelegramClient('my', api_id, api_hash) as client:
#         all_user_group = client.iter_participants(group)
#         async for user in all_user_group:
#             user_full_about = await client(GetFullUserRequest(user))
#             print(user_full_about.full_user.about)
#
#
# asyncio.run(main())