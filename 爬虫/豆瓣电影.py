# -*- codeing = utf-8 -*-
import requests
import json
import pandas as pd
#提示页面
print("""
1-纪录片；2-传记；3-犯罪；4-历史；5-动作；
6-情色；7-歌舞；8-儿童；10-悬疑；11-剧情；
12-灾难；13-爱情；14-音乐；15-冒险；16-奇幻；
17-科幻；18-运动；19-惊悚；20-恐怖；22-战争；
23-短篇；24-喜剧；25-动画；26-同性；27-西部；
28-家庭；29-武侠；30-古装；31-黑色电影
""")
# 获取网址
ua = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"}
website = "https://movie.douban.com/j/chart/top_list"

get_link = input("请选择查询的电影类型：")
get_rank = input("请输入查询的记录数：")
data = {
"type":get_link,
"interval_id":"100:90",
"action":"",
"start":"0",
"limit":get_rank
}
get_website_json = requests.get(url =website,headers = ua,params=data).text
get_website = json.loads(get_website_json)
#获取数据
movie_title = [movie_list['title'] for movie_list in get_website]
movie_score = [movie_list['score'] for movie_list in get_website]
movie_type = [movie_list['types'] for movie_list in get_website]
movie_roles = [movie_list['actors'] for movie_list in get_website]
movie_weburl = [movie_list['url'] for movie_list in get_website]
#下载数据
download_data = pd.DataFrame({"名字":movie_title,"评分":movie_score,"类型":movie_type,"演员":movie_roles,"链接":movie_weburl})
download_data.index = download_data.index + 1
download_data.to_excel("D:/PYTHONSTUDY/pythonProject7/爬虫/movie.xlsx")