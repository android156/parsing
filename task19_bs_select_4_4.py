from bs4 import BeautifulSoup
import requests
import lxml


response = requests.get(url='https://parsinger.ru/4.1/1/index4.html')
response.encoding= 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')

card_names = list(map(BeautifulSoup.get_text, soup.find_all(attrs={'class': ['name_item', 'product_name']})))
for card_name in card_names:
    print(card_name.strip())
