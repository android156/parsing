from bs4 import BeautifulSoup
import requests
import lxml


response = requests.get(url='https://parsinger.ru/4.1/1/index4.html')
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')

li_ids = soup.select('li.description_detail')
for li in li_ids:
    print(li['id'])

# Примеры:
#
#     Тег: select("p")
#     Класс: select(".class")
#     Идентификатор: select("#id")
#     Атрибут: select("[attribute=value]")
#     Несколько селекторов: select("p.class")
#     Вложенные элементы: select("div span")
#     Непосредственные дочерние элементы: select("div > p")
#     Элементы с несколькими классами: select(".class1.class2")
#     Элементы с определенными атрибутами: select("[data-custom]")
#     Псевдоклассы CSS: select("p:first-of-type") или select("p:last-of-type")
#     Соседние элементы: select("h1 + p")
#     Элементы, содержащие определенный текст:
