# https://parsinger.ru/img_download/img/ready/1.png

import requests
import pprint

file_dict = {}

# Создаем сессию
with requests.Session() as s:
    for i in range(1, 201):
        url = f'https://parsinger.ru/img_download/img/ready/{i}.png'
        response = s.get(url)
        if response.status_code == 200:
            file_dict[i] = response.headers.get('Content-Length')
            print(i, file_dict[i])
            with open(f'task_img/image_{i:03d}.png', 'wb') as file:
                file.write(response.content)

sort_dict = sorted(file_dict.items(), key=lambda item: item[1])
pprint.pprint(sort_dict)

# import os
# import re
# from PIL import Image
# import pytesseract
# import requests
# from tqdm import tqdm
#
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
# custom_config = r'--oem 3 --psm 12'
#
# dirname = "images"
# if not os.path.exists(dirname):
#     os.mkdir(dirname)
#
#
# def find_numbers(pic: str):
#     with Image.open(pic) as img:
#         width, height = img.size
#         crop = img.crop((0, height - 20, width // 4, height))
#         result = pytesseract.image_to_string(crop, lang='rus', config=custom_config)
#         reg = re.search(r'\d+', result)
#         if reg:
#             print(f"\nСекретный код в {pic.split('/')[-1]}: {result}")
#
#
# # Инициализация
# for i in tqdm(range(1, 161)):
#     url = f"https://parsinger.ru/img_download/img/ready/{i}.png"
#     response = requests.get(url, stream=True)
#     file_name = f"{dirname}/image_{i:03d}.png"
#     with open(file_name, 'wb') as file:
#         file.write(response.content)
#     find_numbers(file_name)
