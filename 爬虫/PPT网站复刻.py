# -*- codeing = utf-8 -*-
import os
import requests
from lxml import etree
if not os.path.exists('D:/PYTHONSTUDY/pythonProject7/爬虫/kejippt'):
    os.mkdir('D:/PYTHONSTUDY/pythonProject7/爬虫/kejippt')

web = "https://www.1ppt.com/beijing/keji/"
ua = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36'}

get_web = requests.get(url=web,headers=ua)
get_web.encoding = 'gbk'
get_date = etree.HTML(get_web.text)
request_url = get_date.xpath('//ul[@class="tplist"]/li/a/@href')
request_title = get_date.xpath('//dl[@class="dlbox"]//@alt')
request_urls = ['https://www.1ppt.com/' + request_url for request_url in request_url]
# print(all_url)
all_data = dict(zip(request_urls,request_title))
for request_urls,request_title in all_data.items():
    get_web1 = requests.get(url=request_urls,headers = ua).text
    get_date1 = etree.HTML(get_web1)
    request_url1 = get_date1.xpath("//ul[@class='downurllist']/li/a/@href")
    request_url1s = "https://www.1ppt.com" + request_url1[0]
    # print(request_url1s)
    get_web2 = requests.get(url = request_url1s,headers = ua).text
    get_date2 = etree.HTML(get_web2)
    down_load = get_date2.xpath("//li[@class='c1']//a/@href")

    doc_date = requests.get(url=down_load[0],headers =ua).content
    end = down_load[0].split('.')[-1]
    down_garget = 'D:/PYTHONSTUDY/pythonProject7/爬虫/kejippt/' + request_title +'.'+ end
    with open(down_garget,"wb") as i:
        i.write(doc_date)
        print(request_title)

    # print(down_load)