import datetime

from telethon.tl.types import InputMessagesFilterPhotos

from api_info import API_ID, API_HASH
from telethon import TelegramClient, events, sync, connection
import re
from telethon.tl.functions.users import GetFullUserRequest
import asyncio
import pyperclip
import os

url = 'https://t.me/Parsinger_Telethon_Test'




with TelegramClient('my', API_ID, API_HASH, system_version="5.10.7 beta x64") as client:
    all_message = client.get_messages('https://t.me/Parsinger_Telethon_Test', limit=100, filter=InputMessagesFilterPhotos)
    for i, message in enumerate(all_message, start=1):
        text = message.text
        print(f'{i}: {text}')
        client.download_media(message, f'images4/{i}') #file='img/'
        client.send_message('@zamaterevshiy', message)
        if i == 3:
            break



# Метод  .send_message(entity) принимает следующие аргументы:
#
#     entity='username'  -  указывает на пользователя\чат\группу, куда необходимо отправить сообщение, если не указать пользователя, сообщение будет отправлено в чат "Избранное";
#
#     message='text'  - сообщение для отправки или другой объект для отправки, Максимальная длина сообщения составляет 35 000 байт или 4 096 символов;
#
#     reply_to(int\Message) - отвечать на сообщение или нет, если указан int, он должен быть идентификатором сообщения, на которое следует ответить;
#
#     link_preview(=True\False) - должен ли быть включен предварительный просмотр ссылок;
#
#     file(file='C:/file.txt') - отправляет сообщение с вложенным файлом, файл может быть текстовым, видео, аудио или документом и т.д.;
#
#     thumb(str\byte\file) - дополнительный эскиз для отправленного документа;
#
#     force_document(True\False) - отправлять ли данный файл как документ;
#
#     buttons(custom.Button) - отправляет кнопку, которая будет отображаться после отправки сообщения( в данном курсе мы не рассматривали работу с кнопками, кому интересна данная тема, можете самостоятельно почитать в документации )
#
#     silent(True\False) = должно ли сообщение уведомлять людей в широковещательном канале или нет. По умолчанию False, что означает, что он уведомит их. Установите значение True, чтобы изменить это поведение.
#
#     background(True\False) - должно ли сообщение быть отправлено в фоновом режиме.
#
#     schedule(hints.DateLike=None) - устанавливает планировщик для отправки сообщения в указанную дату\время. По умолчанию установлен None, что означает что сообщение будет отправлено немедленно;
#
#     comment_to(int\message) -  оставляет "комментарий"  в широковещательном канале. int, идентификатор паблика\группы. message, сообщение для отправки.

