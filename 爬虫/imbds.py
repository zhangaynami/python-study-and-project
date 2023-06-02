# -*- codeing = utf-8 -*-
import requests
import pandas as pd
from lxml import etree
import time
import json
imbd_250 = 'https://www.imdb.com/chart/top/?ref_=nv_mv_250'
ua = { "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"}

# user_num = int(input("请输入要提取的排名数"))
get_web = requests.get(url = imbd_250,headers = ua).text
# print(get_web)
get_data = etree.HTML(get_web)
# print(get_data)
movie_link = get_data.xpath('//td[@class="titleColumn"]/a/@href')
for i in range(240,250):
    li = 'https://www.imdb.com' + movie_link[i] #详情网址
    get_mov_detail = requests.get(url = li ,headers = ua).text
    get_data1 = etree.HTML(get_mov_detail)

    movie_title = get_data1.xpath('//*[@id="__next"]/main/div/section[1]/section/div[3]/section/section/div[2]/div[1]/h1/text()')

    # print(movie_title) #标题
    movie_time = get_data1.xpath('//*[@id="__next"]/main/div/section[1]/section/div[3]/section/section/div[2]/div[1]/div/ul/li[3]//text()')
    movie_time = ''.join(movie_time)
    # print(movie_time) #时长
    movie_director = get_data1.xpath('//*[@id="__next"]/main/div/section[1]/div/section/div/div[1]/section[4]/ul/li[1]/div/ul/li/a/text()')
    movie_director = ','.join(movie_director)
    # print(movie_director)  导演
    movie_writer = get_data1.xpath('//*[@id="__next"]/main/div/section[1]/div/section/div/div[1]/section[4]/ul/li[2]/div/ul/li/a/text()')
    movie_writer = ','.join(movie_writer)
    # print(movie_writer) #编剧
    movie_genres = get_data1.xpath('//*[@id="__next"]/main/div/section[1]/section/div[3]/section/section/div[3]/div[2]/div[1]/div[1]/div/div[2]//text()')
    movie_genres = ','.join(movie_genres)
    # print(movie_genres) #类型
    print("捕获",movie_title)

    mov_data = pd.DataFrame({"标题":movie_title,"时长":movie_time,"导演":movie_director,"编剧":movie_writer,"类型":movie_genres})
    mov_data.to_csv("D:/PYTHONSTUDY/pythonProject7/imbd250_list.csv",index=False,header=0,mode='a',encoding='ANSI')
