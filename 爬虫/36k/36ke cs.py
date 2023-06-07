# -*- codeing = utf-8 -*-
import requests
from bs4 import BeautifulSoup

url = "https://www.36kr.com/search/articles/mr"
params = {"per_page": "20", "page": "1"}

while True:
    response = requests.get(url, params=params)
    soup = BeautifulSoup(response.content, "html.parser")
    articles = soup.find_all("div", class_="article-item")

    for article in articles:
        title = article.find("a", class_="article-item-title").get_text().strip()
        link = article.find("a", class_="article-item-title").get("href")
        summary = article.find("p", class_="article-item-summary").get_text().strip()
        print("标题：", title)
        print("链接：", link)
        print("概述：", summary)
        print()

    # 判断是否有下一页
    next_page = soup.find("a", class_="kr-pager-next")
    if next_page is None:
        break

    # 更新参数，翻页
    params["page"] = str(int(params["page"]) + 1)