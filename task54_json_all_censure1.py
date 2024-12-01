import requests
from bs4 import BeautifulSoup as bs
import json
import re


session = requests.Session()
scheme = "https://parsinger.ru/html/"


def get_soup(link):
    global session
    try:
        response = session.get(link)
        response.raise_for_status() # поднятие ошибки, если будут проблемы при запросе
        response.encoding = "utf-8"
        return bs(response.text, "lxml")
    except requests.HTTPError as e:
        print(e)


def getPages(link):
    soup1 = get_soup(link)
    categories = [(f"{scheme}{a.get('href')}", a.find("div")) for a in soup1.find("div", class_="nav_menu").find_all("a", href=re.compile(r"^index\d+.+"))] # получение всех ссылок на категории
    all_pages = []
    for category in categories:
        soup2 = get_soup(category[0])
        pages = [(f"{scheme}{a.get('href')}", category[-1].get_text(strip=True)) for a in soup2.find("div", class_="pagen").find_all("a")] # нахождение всех ссылок на каждую страницу каждой категории
        all_pages.extend(pages)
    return all_pages


def get_info(pages):
    res = []
    for page, category_name in pages:
        soup1 = get_soup(page)
        cards = soup1.find_all("div", class_="item")
        for card in cards:
            link = scheme + card.find("a").get("href") # создание полной ссылки на отдельный товар
            soup2 = get_soup(link)
            # заполнение информацией
            d = {"categories": category_name}
            name = soup2.find("p", id="p_header").get_text(strip=True)
            article = soup2.find("p", class_="article").string.split(": ")[-1].strip()
            d["name"] = name
            d["article"] = article
            description = {}
            descr = soup2.find("ul", id="description")
            for li in descr.find_all("li"):
                key, val = li.get("id"), li.string.split(": ")[-1].strip()
                description[key] = val
            d["description"] = description
            d["count"] = soup2.find("span", id="in_stock").string.split(": ")[-1].strip()
            for span in soup2.find("div", class_="sale").find_all("span"):
                key, val = span.get("id"), span.string.strip()
                d[key] = val
            d["link"] = link
            res.append(d)
    return res


def main():
    url = "https://parsinger.ru/html/index1_page_1.html"
    pages = getPages(url)
    json_result = get_info(pages)
    with open("res.json", "w", encoding="utf-8") as json_file: # запись в файл
        json.dump(json_result, json_file, indent=4, ensure_ascii=False)


try:
    main()
finally:
    session.close()