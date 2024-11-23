import requests
from random import choice
from time import sleep
from bs4 import BeautifulSoup
from fake_useragent import UserAgent


headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest'
}

url = "https://bitality.cc/Home/GetSum?GiveName=Ethereum&GetName=Bitcoin&Sum=4.1895414&Direction=0"
response = requests.get(url=url, headers=headers).json()
print(response)



headers = {'user-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:106.0) Gecko/20100101 Firefox/106.0',
           'X-Requested-With': 'XMLHttpRequest', }

url = 'https://cbr.ru/Queries/AjaxDataSource/112805'

data_dollar = {
    'DT': '',
    'val_id': 'R01235',
    '_': '1667219511852'
}
data_euro = {
    'DT': '',
    'val_id': 'R01239',
    '_': '1667219511853'
}
response_dollar = requests.get(url=url, headers=headers, params=data_dollar).json()[-1]
response_euro = requests.get(url=url, headers=headers, params=data_euro).json()[-1]

print(f'Дата: {response_dollar["data"][:10]}')
print(f'Курс USD: {response_dollar["curs"]} рублей')
print(f'Курс EUR: {response_euro["curs"]} рублей')


ua = UserAgent(min_percentage=25)

headers = {'user-agent': ua.random,
           'x-requested-with': 'XMLHttpRequest'}

url = 'https://bitality.cc/Home/'
response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, 'lxml')
# ('span', class_="ml-2 b-choose__item-txt")]
banks = [value['data-name'] for value in soup.find_all('div', {'data-exchange-ps-type': 'bank'})]
crypts = [value['data-name'] for value in soup.find_all('div', {'data-exchange-ps-type': 'crypto'})]


while True:
    v1 = choice(banks)
    v2 = choice(crypts)
    if v1 == v2:
        continue
    url = f"https://bitality.cc/Home/GetSum?GiveName={v1}&GetName={v2}&Sum=1&Direction=0?"
    response = requests.get(url=url, headers=headers, proxies={"http": "http://15.235.153.57:8089"}).json()

    print(f"{response['giveSum']} {v1} = {response['getSum']} {v2}")
    sleep(3)