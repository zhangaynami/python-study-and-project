# -*- codeing = utf-8 -*-
import requests
import json
import os
import time
ua = {
    "user_agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
    'Referer': 'http://www.kuwo.cn/search/list?key=%E5%91%A8%E6%9D%B0%E4%BC%A6',
    'csrf': 'RUJ53PGJ4ZD',
    'Cookie': 'Hm_lvt_cdb524f42f0ce19b169a8071123a4797=1577029678,1577034191,1577034210,1577076651;Hm_lpvt_cdb524f42f0ce19b169a8071123a4797=1577080777; kw_token=RUJ53PGJ4ZD'
    }

singer_name = input("请输入歌手姓名:")
sing_num = int(input("请输入要下载的页数:"))
if not os.path.exists(f"D:/PYTHONSTUDY/pythonProject7/爬虫/singer/{singer_name}"):
    os.mkdir(f"D:/PYTHONSTUDY/pythonProject7/爬虫/singer/{singer_name}")
for pages in range(1,sing_num+1):
    singer_web = f"https://www.kuwo.cn/api/www/search/searchMusicBykeyWord?key={singer_name}&pn={pages}&rn=30&httpsStatus=1&reqId=4458f5c0-9c9e-11ed-b6ce-cf755f63f196"
    get_singsweb = requests.get(url=singer_web,headers = ua).text
    get_sings = json.loads(get_singsweb)
    # print(get_sings)
    get_sing =get_sings['data']['list']
    # print(get_sing)
    for i in get_sing:
        sings_name = i['name']
        sings_code = i['rid']
        # print(get_sing)
        singurl = f"https://www.kuwo.cn/api/v1/www/music/playUrl?mid={sings_code}&type=music&httpsStatus=1&reqId=e2ecd731-9ca6-11ed-8f2c-f558ab25de0e"
        # print(singurl)
        get_singweb1 = requests.get(url =singurl,headers= ua).text
        # print(get_singweb1)
        get_singweb2 = json.loads(get_singweb1)

        while get_singweb2['code'] == -1:
            print(f'{sings_name}是vip歌曲,无法下载')
            time.sleep(3)
            break
        else:

            get_sings1 = get_singweb2["data"]['url']
            download = requests.get(url=get_sings1).content
            downlad_path = f"D:/PYTHONSTUDY/pythonProject7/爬虫/singer/{singer_name}/{sings_name}.mp3"
            with open(downlad_path,"wb") as i:
                i.write(download)
                print(sings_name,"下载成功")
            time.sleep(3)