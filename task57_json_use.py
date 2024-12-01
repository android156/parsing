from pprint import pprint
import pyperclip
import requests

url = 'http://parsinger.ru/downloads/get_json/res.json'

res = {}

response = requests.get(url=url).json()
for item in response:
    # pprint(item)
    # print(int(res.get(item['count'], 0)))
    # break
    if res.get(item['categories']):
        res[item['categories']] += int(item.get('count', 0))
    else:
        res[item['categories']] = int(item.get('count', 0))

pprint(res)
pyperclip.copy(res)