import requests
from bs4 import BeautifulSoup
import pandas as pd
import pyperclip # запись в буфер обмена.



url = 'https://parsinger.ru/4.8/8/index.html'
response = requests.get(url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'html.parser')

colspans = soup.find_all(colspan=True)
# colspans = soup.select("td[colspan]")

print(sum([int(colspan.text) for colspan in colspans if colspan.text.strip().isalnum()]))



