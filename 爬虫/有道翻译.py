# -*- codeing = utf-8 -*-
import json

import pandas as pd
import requests

print("退出请输入quit")
while True:
    your_input = input("请输入要翻译的内容：")
    if  your_input == 'quit':
        break
    else:
        youdao = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
        ua = {"user_agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"}
        # get_website = requests.post(url=youdao,headers = ua).text
        get_website_json = requests.post(url=youdao,headers = ua).text
        data = {}
        data["i"] = your_input
        data["doctype"] = "json"
        data["from"] = "AUTO"
        data["to"] = "AUTO"
        data["client"] = "fanyideskweb"

        # print(data)
        get_website_json = requests.post(url=youdao,data = data,headers = ua).text

        # print(get_website_json)
        get_website = json.loads(get_website_json)
        # print(get_website)
        from_you  = get_website['translateResult'][0][0]['src']
        grt_you = get_website['translateResult'][0][0]['tgt']
        return_data = pd.DataFrame({"A":[your_input],"B":[grt_you]})
        return_data.to_csv('D:/PYTHONSTUDY/pythonProject7/爬虫/翻译.csv',index=False,header=0,mode='a',encoding='ANSI')