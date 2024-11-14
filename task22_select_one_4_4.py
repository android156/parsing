from bs4 import BeautifulSoup
import requests
import lxml


response = requests.get(url='https://parsinger.ru/4.1/1/index6.html')
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')

section3 = soup.select_one('section#section3 p').next_sibling.text.strip()

print(section3)

# Примеры:
#
#     Тег: select_one("p")
#     Класс: select_one(".class")
#     Идентификатор: select_one("#id")
#     Атрибут: select_one("[attribute=value]")
#     Несколько селекторов: select_one("p.class")
#     Вложенные элементы: select_one("div span")
#     Непосредственные дочерние элементы: select_one("div > p")
#     Элементы с несколькими классами: select_one(".class1.class2")
#     Элементы с определенными атрибутами: select_one("[data-custom]")
#     Псевдоклассы CSS: select_one("p:first-of-type") или select_one("p:last-of-type")
#     Соседние элементы: select_one("h1 + p")
