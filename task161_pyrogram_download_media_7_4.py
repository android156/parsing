from pyrogram import Client
from pyrogram.enums import MessagesFilter
from tqdm import tqdm


api_id = 25300378
api_hash = "b1d1f4c93bf8f885a884030878eaa9bc"

app = Client("my_session", api_id=api_id, api_hash=api_hash)

group_url = 'parsinger_pyrogram'  # Например, можно использовать @username для публичных каналов или чатов

def progress(current, total, progress_bar):
    # Обновляем прогресс-бар
    progress_bar.update(current - progress_bar.n)

def main():
    with app:
        for message in app.get_chat_history(group_url):
            if message.media:
                file_name = f"media/{message.id}"
                file_size = None

                # Определение расширения файла и размера в зависимости от типа медиа
                if message.photo:
                    file_name += ".jpg"
                    file_size = message.photo.file_size
                elif message.video:
                    file_name += ".mp4"
                    file_size = message.video.file_size
                elif message.audio:
                    file_name += ".mp3"
                    file_size = message.audio.file_size
                elif message.document:
                    file_name += f".{message.document.mime_type.split('/')[-1]}"
                    file_size = message.document.file_size
                elif message.voice:
                    file_name += ".ogg"
                    file_size = message.voice.file_size
                elif message.video_note:
                    file_name += ".mp4"
                    file_size = message.video_note.file_size
                elif message.sticker:
                    file_name += ".webp"
                    file_size = message.sticker.file_size
                elif message.animation:
                    file_name += ".mp4"
                    file_size = message.animation.file_size

                # Создание прогресс-бара для каждого файла
                # Если размер файла определен, создаем прогресс-бар и начинаем загрузку
                if file_size:
                    with tqdm(total=file_size, unit='B', unit_scale=True, desc="Скачивание") as progress_bar:
                        app.download_media(message, file_name=file_name, progress=progress, progress_args=(progress_bar,))

main()

#
#
#
#     audio: Аудиофайлы или музыкальные треки.
#
#     # Проверка наличия аудио в сообщении
#     if message.audio:
#         # Скачиваем аудио
#         app.download_media(message.audio, file_name=f"audio/{message.message_id}.mp3")
#
#
#
#     document: Документы, такие как PDF, Word или любые другие файлы, которые не подпадают под другие медиа-категории.
#
#     # Проверка наличия документа в сообщении
#     if message.document:
#         # Скачиваем документ
#         app.download_media(message.document, file_name=f"documents/{message.message_id}_{message.document.file_name}")
#
#
#
#     photo: Фотографии или изображения.
#
#     # Проверка наличия фотографии в сообщении
#     if message.photo:
#         # Скачиваем фотографию
#         app.download_media(message.photo, file_name=f"photos/{message.message_id}.jpg")
#
#
#
#     sticker: Стикеры, используемые в Telegram для выражения эмоций или реакций.
#
#     # Проверка наличия стикера в сообщении
#     if message.sticker:
#         # Скачиваем стикер
#         app.download_media(message.sticker, file_name=f"stickers/{message.message_id}.webp")
#
#
#
#     animation: Гифки или анимированные изображения.
#
#     # Проверка наличия анимации (гифки) в сообщении
#     if message.animation:
#         # Скачиваем анимацию
#         app.download_media(message.animation, file_name=f"animations/{message.message_id}.mp4")
#
#
#
#     video: Видеофайлы.
#
#     # Проверка наличия видео в сообщении
#     if message.video:
#         # Скачиваем видео
#         app.download_media(message.video, file_name=f"videos/{message.message_id}.mp4")
#
#
#
#     voice: Голосовые сообщения.
#
#     # Проверка наличия голосового сообщения
#     if message.voice:
#         # Скачиваем голосовое сообщение
#         app.download_media(message.voice, file_name=f"voice/{message.message_id}.ogg")
#
#
#
#     video_note: Круглые видео сообщения, которые обычно короткие и записываются через камеру фронтального вида.
#
#     # Проверка наличия видеосообщения
#     if message.video_note:
#         # Скачиваем видеосообщение
#         app.download_media(message.video_note, file_name=f"video_notes/{message.message_id}.mp4")
#
#
#
#     new_chat_photo: Фотографии, которые установлены как новые изображения профиля чата.
#
#     # Проверка наличия новой фотографии чата в сообщении
#     if message.new_chat_photo:
#         # Скачиваем новую фотографию чата
#         app.download_media(message.new_chat_photo, file_name=f"chat_photos/{message.message_id}.jpg")


