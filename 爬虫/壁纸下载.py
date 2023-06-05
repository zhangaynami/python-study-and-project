# -*- codeing = utf-8 -*-
from bs4 import BeautifulSoup
import os
import requests
page_n = int(input('请输入爬取的页数:'))
# sec_id = int(input('输入图片searchid'))
doc = input('请输入所属文件')

if not os.path.exists(f'D:/文档/壁纸下载/{doc}'):
    os.mkdir(f'D:/文档/壁纸下载/{doc}')

for page_num in range(1,page_n+1):
    ua = { "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"}
    wallerpaper_web = f'https://wallhaven.cc/search?q=blue%20archive&categories=110&purity=100&sorting=relevance&order=desc&page={page_num}'  #替换所需内容

    get_web = requests.get(url = wallerpaper_web,headers = ua).text
    page = BeautifulSoup(get_web,'html.parser')
    image_text = page.find('section', class_="thumb-listing-page")
    # print(image_text)
    mic_link = image_text.find_all('a',class_="preview")
    # print(mic_link)
    all_link =[]
    for i in mic_link:

        pic = i['href']
        all_link.append(pic)
    # print(all_link)
    for i in all_link:
        get_pic = requests.get(url=i, headers=ua)
        get_pic.encoding = "gbk"
        get_url = BeautifulSoup(get_pic.text,'html.parser')
        pic_link = get_url.find('div',class_="scrollbox")
        pic_link = pic_link.find_all('img')
        # print(pic_link)

        for x in pic_link:
            pic_name = x['data-wallpaper-id']
            pic_link = x['src']
            # print(pic_name,pic_link)
            print(pic_name + '下载成功')
            pic_link_down = requests.get(url = pic_link).content


            end = pic_link.split('.')[-1]
            # print(end)
            down_load = f'D:/文档/壁纸下载/{doc}/' + pic_name +'.' + end
            print(down_load)
            with open(down_load,'wb') as y:
                y.write(pic_link_down)