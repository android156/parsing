
# Библиотеки уже импортированы:
from bs4 import BeautifulSoup
import requests
url = "https://parsinger.ru/4.3/4/index.html"

def del_spaces(my_str):
    return my_str.replace(" ", "")

def check_even_len(my_str):
    return len(my_str) % 2 == 0

def sum_even_length_ids(html):

    soup = BeautifulSoup(html, 'html.parser')
    tag_p_list = soup.find_all('p')
    id_values_list = [int(p.get('id')) + int(p.get('class')[0]) for p in tag_p_list if check_even_len(del_spaces(p.text))]
    # map(BeautifulSoup.get_text, soup.find_all('p'))
    print(tag_p_list)
    print(id_values_list)

    print(f"Сумма ID и CLASS тегов <p> с чётной длиной текста без пробелов: {sum(id_values_list)}")


response = requests.get(url)
html = response.content
sum_even_length_ids(html)