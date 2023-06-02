# -*- codeing = utf-8 -*-
import requests #webmessage
from lxml import etree #download message
import pandas as pd
target_net = "https://www.jkl.com.cn/shop.aspx"
ua = {"user_agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"}



#1  拿取地区网址
request_data = requests.get(url = target_net , headers = ua).text #取得文字信息
# print(request_data)
read_data = etree.HTML(request_data) #j解析数据
downtown = read_data.xpath('//div[@class="infoLis"]//@href') #获取下级网址
# print(downtown)
for i in downtown:
    web_data1 = "https://www.jkl.com.cn/" +  i
    request_data1 = requests.get(url = web_data1,headers = ua).text #取得文字信息
    read_data1 = etree.HTML(request_data1)  #j解析数据
    shop = read_data1.xpath("//span[@class='con01']/text()")
    place = read_data1.xpath("//span[@class='con02']/text()")
    phone = read_data1.xpath("//span[@class='con03']/text()")
    keeptime = read_data1.xpath("//span[@class='con04']/text()")
    # print(shop,place,phone,keeptime)
    print(shop,place,phone,keeptime)
    data_list = []
    for shop1 in shop:
        shop2 = shop1.strip() #去符号
        data_list.append(shop2)
    print(shop, place, phone, keeptime)
    target_date = pd.DataFrame({"店名":data_list,"地址":place,"电话":phone,"时间":keeptime})
    target_date.to_csv("D:/PYTHONSTUDY/pythonProject7/爬虫/shopname.csv",index=False,header=0,mode='a',encoding='ANSI')