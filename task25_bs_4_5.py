import re

from bs4 import BeautifulSoup
import requests
import lxml


def get_num_value(my_text):
    found_float = re.search(r'\d+(?:\.\d+)?', my_text)
    if found_float:
        return float(found_float.group())


response = requests.get(url='https://parsinger.ru/html/index1_page_1.html')
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')

prices = soup.select('div.price_box p.price')
prices = [get_num_value(price.text) for price in prices]
print(sum(prices))


