import datetime
from api_info import API_ID, API_HASH
from telethon import TelegramClient, events, sync, connection
import re
from telethon.tl.functions.users import GetFullUserRequest
import asyncio
import pyperclip
import os

url = 'https://t.me/Parsinger_Telethon_Test'

def get_num_art(art):
    art_num = re.search(r'\d+', art)
    if art_num:
        return int(art_num.group())
    return 0


usernames = []
with TelegramClient('my', API_ID, API_HASH, system_version="5.10.7 beta x64") as client:
    all_message = client.get_messages('https://t.me/Parsinger_Telethon_Test', limit=100, )
    for i, message in enumerate(all_message, start=1):
        text = message.text
        print(f'{i}: {text}')
        if text:
            number = get_num_art(text)
            if number:
                id_user = message.from_id.user_id
                username = client.get_entity(id_user).username
                if not username in usernames:
                    usernames.append(username)
print(usernames)
pyperclip.copy(usernames)



# Message(
#     id=200, - идентификатор этого сообщения;
#     peer_id=
#         PeerChannel(
#             channel_id=1795821154), - ID пользователя, группы, канала,  куда было отправлено сообщение;)
#     date=
#         datetime.datetime(2022, 6, 11, 9, 40, 26, tzinfo=datetime.timezone.utc), - объект даты, указывает на то, когда сообщение было отправлено;
#     message='Текст сообщения', - строковый объект сообщения;
#     out=False, - возвращает True, если сообщение является исходящим, т.е., отправлено с вашей учетной записи;
#     mentioned=False, - возвращает True, если, вы были упомянуты в этом сообщении;
#     media_unread=False,  - возвращает True, если медиа в сообщении не были прочитаны;
#     silent=False, - возвращает True, если уведомления отключены;
#     post=False,  - возвращает True, если сообщение является постом в широковещательном канале;
#     from_scheduled=False,  - возвращает True, если сообщение было создано из заранее запланированного сообщения;
#     legacy=False,  - возвращает True, если сообщение является устаревшим;
#     edit_hide=False,  - возвращает True, если метка о редактировании сообщения была скрыта;
#     pinned=False,   - возвращает True, если сообщение закреплено в настоящее время;
#     from_id=
#         PeerUser(
#             user_id=5125814085),  - ID пользователя, группы или канала отправившего сообщение;
#     fwd_from=None,  - возвращает True, если сообщение является репостом из другого чата\группы\паблика;
#     via_bot_id=None,   - ID бота который отправлял это сообщение;
#     reply_to=None,  - ID  сообщения если это сообщение отвечает на другое;
#     media=None, - медиафайлы отправленные в сообщении если такие имеются(фото, видео, документы, GIF, стикеры и т.д)
#     reply_markup=None, - разметка для этого сообщения, которое отправлено ботом, чаще всего это кнопки;
#     entities=[], - список элементов в этом сообщении, таких как жирный шрифт, курсив, код, гиперссылки и т.д.;
#     views=None, - количество просмотров этого сообщения;
#     forwards=None, - сколько раз это сообщение было переадресовано;
#     replies= - сколько раз другое сообщение ответило на это сообщение;
#         MessageReplies(
#             replies=0,
#             replies_pts=213,
#             comments=False,
#             recent_repliers=[],
#             channel_id=None,
#             max_id=None,
#             read_max_id=None),
#     edit_date=None, - дата последнего редактирования сообщения;
#     post_author=None, - отображаемое имя отправителя сообщения;
#     grouped_id=None, - проверяет, принадлежит ли это сообщение к группе сообщений, фото- или видео альбому;
#     restriction_reason=[], - список причин, по которым это сообщение было ограничено;
#     ttl_period=None - период жизни, настроенный для этого сообщения;)
#
#
# .get_messages() и .iter_messages()принимают одинаковые аргументы:
#
#     client.get_messages(chat\group\dialog) - первый обязательный аргумент, ссылка на телеграмм чат\паблик\диалог;
#     client.get_messages(limit) - количество сообщений, которые необходимо собрать из группы\паблика\диалога, если limit не установлен, будет получено первое сообщение в чате, так как по умолчанию установлен вывод всего одного сообщения, однако если указать limit=None, то должны быть получены все сообщения. Однако limit=None следует использовать с осторожностью, так как попытка получения слишком большого количества сообщений может быть расценена как подозрительная и может привести к временной блокировке или ограничению запросов от Telegram API.
#
#     client.get_messages(offset_date=datetime(2022, 6, 1)) - принимает объект datatime находит все сообщения ранее указанной даты, формат даты(год, месяц, день);
#
#     client.get_messages(offset_id(id_message)) - будут извлечены те сообщения, которые предшествуют сообщению с указанным id_message;
#
#     client.get_messages(max_id=30) - будут исключены те сообщения, которые имеют более высокий идентификатор;
#
#     client.get_messages(min_id=30) - будут исключены  те сообщения, которые имеют более старый идентификатор;
#
#     client.get_messages(search='Искомый текст') - строка, которая будет использоваться в качестве поискового запроса;
#
#     client.get_messages(from_user="@user") -будут возвращены сообщения только этого пользователя. Имя можно указать как username, id_user, last_name, first_name;
#
#     client.get_message(reverse=True) - Если установлено значение True, сообщения будут возвращаться в обратном порядке (от самого старого к самому новому, а не от нового к самому старому). Это также означает, что значения параметров offset_id и offset_date меняются местами;
#     client.get_messages(filter=InputMessagesFilterPhotos) - фильтр используется для возврата сообщения. Например, данный фильтр вернет первое сообщение содержащее фото. Для работы с подобными фильтрами необходимо их импортировать from telethon.tl.types import InputMessagesFilterPhotos.
#     Другие используемые фильтры (у каждого фильтра в списке, свой одноимённый импорт, по аналогии с InputMessagesFilterPhotos):
#         filter=InputMessagesFilterChatPhotos- вернет первое сообщение, содержащее фото;
#         filter=InputMessagesFilterContacts- вернет первое сообщение, содержащее контакт пользователя;
#         filter=InputMessagesFilterDocument- вернет первое сообщение, содержащее документ(pdf, docx, txt т т.д.);
#         filter=InputMessagesFilterEmpty- вернет первое  сообщение, если его отправитель пуст, скорее всего это работает если пользователь был забанен в группе, а его сообщения не удалены;
#         filter=InputMessagesFilterGeo- вернет первое сообщение, в котором есть геометка;
#         filter=InputMessagesFilterGif- вернет первое сообщение, в котором содержится GIF;
#         filter=InputMessagesFilterMusic- вернет первое сообщение, если в нём содержится музыкальный файл;
#         filter=InputMessagesFilterMyMentions- вернет первое сообщение, в котором есть упоминания учетной записи, с которой происходит поиск;
#         filter=InputMessagesFilterPhoneCalls- вернет информацию об аудио-звонке;
#         filter=InputMessagesFilterPhotoVideo- вернет информацию о видео-звонке;
#         filter=InputMessagesFilterPhotos- используется для фильтрации результатов при поиске сообщений, чтобы получить только сообщения, содержащие фотографии;
#         filter=InputMessagesFilterPinned- вернет первое закреплённое сообщение;
#         filter=InputMessagesFilterRoundVideo- вернет первое сообщение, в котором содержится  круглое видео;
#         filter=InputMessagesFilterRoundVoice- вернет первое сообщение, в котором содержится голосовое сообщение;
#         filter=InputMessagesFilterUrl- вернет первое сообщение, в котором содержится ссылка;
#         filter=InputMessagesFilterVideo-  вернет первое сообщение, в котором содержится видео;
#         filter=InputMessagesFilterVoice- вернет первое сообщение, в котором содержится голосовое сообщение.
