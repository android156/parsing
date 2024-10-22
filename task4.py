import requests

url = 'https://parsinger.ru/video_downloads/videoplayback.mp4'
# Выполняем GET-запрос к указанному URL с параметром stream=True.
# Параметр stream=True гарантирует, что соединение будет удерживаться, пока не будут получены все данные.
response = requests.get(url=url, stream=True)

# Открываем (или создаем) файл 'file.mp4' в режиме 'wb' (write binary),
# чтобы сохранить в него бинарные данные.
with open('file.mp4', 'wb') as file:

    # Записываем содержимое ответа (response.content) в файл.
    # Этот метод подходит для относительно небольших файлов,
    # так как все содержимое файла сначала загружается в оперативную память.
    file.write(response.content)

# Если файл здоровый и оперативка не позволяет скачать так много одним куском, то бьем все на чанки
# with open('file.mp4', 'wb') as video:
#     for piece in response.iter_content(chunk_size=100000):
#         video.write(piece)

