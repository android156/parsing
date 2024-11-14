from bs4 import BeautifulSoup
import requests
import lxml


response = requests.get(url='https://parsinger.ru/4.1/1/index5.html')
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')

emails = soup.select('div.email_field')

res = [email.select_one('strong').nextSibling.text.strip() for email in emails]

# Варианты
# emails = soup.select('.email_field strong')
# emails = [tag.next_sibling.strip() for tag in emails]

# Нахождение всех блоков с электронной почтой
# email_blocks = soup.find_all('div', class_='email_field')

# Извлечение адресов электронной почты
# emails = [block.strong.next_sibling.strip() for block in email_blocks]

# email_fields = soup.select('div.email_field > strong')

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
