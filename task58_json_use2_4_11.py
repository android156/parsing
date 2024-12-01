from collections import OrderedDict
from pprint import pprint
import pyperclip
import requests
import re

def get_num_value(my_text):
    found_float = re.search(r'\d+(?:\.\d+)?', my_text)
    if found_float:
        return float(found_float.group())


url = 'https://parsinger.ru/downloads/get_json/res.json'

res = OrderedDict()

response = requests.get(url=url).json()
for i, item in enumerate(response, start=2):

    if res.get(item['categories']):
        res[item['categories']] += int(item.get('count', 0)) * int(get_num_value(item.get('price', 0)))
    else:
        res[item['categories']] = int(item.get('count', 0)) * int(get_num_value(item.get('price', 0)))
    if i == 1:
        pprint(item)
        pprint(res)
        break


pprint(res)
pyperclip.copy(dict(res))