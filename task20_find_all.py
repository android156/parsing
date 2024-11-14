from bs4 import BeautifulSoup
import requests
import lxml


def del_no_digit(my_str):
    only_digits_str = ''
    for sym in my_str:
        if sym.isdigit():
            only_digits_str += sym
    return only_digits_str


response = requests.get(url='https://parsinger.ru/4.1/1/index4.html')
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')

prices = list(map(BeautifulSoup.get_text, soup.find_all('p', attrs={'class': ['price', 'product_price']})))
total_price = 0
for price in prices:
    total_price += int(del_no_digit(price))

print(total_price)