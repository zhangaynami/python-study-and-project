# -*- codeing = utf-8 -*-

import re

import pandas as pd
import requests

ua = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'}
ygdy = 'https://m.ygdy8.com'

get_web = requests.get(url = ygdy,headers =ua,verify=False)
get_web.encoding = 'gb2312'
print(get_web)
re1 = re.compile(r'迅雷电影资源.*?<ul>(?P<text>.*?)</ul>',re.S)
re2 =re.compile(r"迅雷电影资源.*?<a href='(?P<link>.*?)'")
get_re1 = re1.finditer(get_web.text)


all_urls = []
for i in get_re1:
    ul = i.group("text")

    get_re2 =re2.finditer(ul)
    for x in get_re2:
        ul1 = x.group("link")
        all_url = 'https://m.ygdy8.com' + ul1
        all_urls.append(all_url)

for i in all_urls:
    get_web1 = requests.get(url=i, headers=ua, verify=False)
    get_web1.encoding = 'gb2312'
    #爬片名和电影链接
    re3 = re.compile(r'◎译　　名(?P<tit>.*?)<br />.*?'
                     r'<a target="_blank" href="(?P<mlink>.*?)">',
                     re.S)
    get_re2 = re3.finditer(get_web1.text)
    for x in get_re2:

        dic = x.groupdict()

        down_link = 'D:/PYTHONSTUDY/pythonProject7/爬虫/re模块/阳光电影1.csv'
        download = pd.DataFrame(dic,index=[0])
        download.to_csv(down_link,mode='a',header=0,index=False,encoding='ANSI')
