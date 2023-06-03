# -*- codeing = utf-8 -*-
import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://movie.douban.com/cinema/nowplaying/xiamen/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}
response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, 'html.parser')
soup = soup.find_all("ul","class"=="lists")[2]
soups = soup.find_all('li',class_="list-item")
# print(soups)
movies = []
for movie in soups:
    title = movie["data-title"]
    rating = movie["data-score"]
    release_date = movie["data-release"]
    director = movie["data-director"]
    actors = movie["data-actors"]
    duration = movie["data-duration"]
    link = movie.find("a")["href"]
    data = {
        '电影名': title,
        '评分': rating,
        '上映时间': release_date,
        '导演': director,
        '演员': ''.join(actors),
        "时长":duration,
        '链接': link
    }
    movies.append(data)
# print(movies)
df = pd.DataFrame(movies)
df.to_excel('douban_movies.xlsx', index=False)

