import requests
import json
import time
import random
import hashlib
url = 'https://fanyi.youdao.com/bbk/translate_m.do'
# 设置请求头信息
headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Host': 'fanyi.youdao.com',
    'Origin': 'https://fanyi.youdao.com',
    'Referer': 'https://fanyi.youdao.com/index.html',

    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="8"',
    'sec-ch-ua-mobile': '?0',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
    'cookie':"OUTFOX_SEARCH_USER_ID=1509705023@112.48.44.126; OUTFOX_SEARCH_USER_ID_NCOO=615818565.2621735; _ntes_nnid=2782833bed6bc1ce4574f31ca4738176,1626095120357; _ga=GA1.2.693715886.1644477092; __yadk_uid=5BIMaiM2WW9lfSUdoHH8XzqEZlTqFKQO"
}
# 设置请求参数
translation_words = '周末愉快'
ts = str(int(time.time() * 1000))
salt = ts + str(random.randrange(0,10))
from_data = {
    "i": translation_words ,

    "tgt": "I",
    "from": "zh-CHS",
    "to": "en",
    "client": "fanyideskweb",
    "salt": salt,
    "sign": hashlib.md5(("fanyideskweb" + translation_words + salt + "Ygy_4c=r#e#4EX^NUGUc5").encode('utf-8')).hexdigest(),
    "ts": ts,
    "bv": "006f8f26e6ad31a24ea90b6e39e7799e",
    "doctype": "json",
    "version": "3.0",
    "cache": "true"
}
# 发送 POST 请求
response = requests.post(url, headers=headers, data=from_data).json()
print(response)
# 解析响应结果
# response1 = json.loads(response)
# print(response1)