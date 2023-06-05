# -*- codeing = utf-8 -*-
# -*- codeing = utf-8 -*-
import pandas as pd
import requests
import openpyxl
import json
import time
import pandas as pa
product_code = input(r"请输入商品编ma:")
page_code = input(r"请输入页码:")
website = f'https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId={product_code}&score=0&sortType=5&page={int(page_code)-1}&pageSize=10&isShadowSku=0&fold=1'
ua = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"}
get_data = requests.get(url=website,headers=ua).text
# print(get_data)
get_data = get_data.replace('fetchJSON_comment98(','')
get_data = get_data.replace(');','')
# print(get_data)

dic_data = json.loads(get_data)

comment_list = dic_data["comments"]
max_page = dic_data["maxPage"]
print(max_page)
for page in range(0,max_page):
    website = f'https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId={product_code}&score=0&sortType=5&page={page-1}&pageSize=10&isShadowSku=0&fold=1'
    get_data = requests.get(url=website, headers=ua).text
    # print(get_data)
    get_data = get_data.replace('fetchJSON_comment98(', '')
    get_data = get_data.replace(');', '')
    # print(get_data)
    dic_data = json.loads(get_data)
    text = [comment['content'] for comment in comment_list]
    color = [comment['productColor'] for comment in comment_list]
    # print(color)
    use_data = pd.DataFrame({"text":text,"color":color})
    use_data.index = use_data.index+1
    use_data.to_csv('D:/PYTHONSTUDY/pythonProject7/爬虫/jd.csv',mode='a',header=0,encoding ='ANSI')
    time.sleep(3)