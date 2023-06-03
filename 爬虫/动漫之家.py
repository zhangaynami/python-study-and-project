# -*- codeing = utf-8 -*-
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
import xlwt

wb = xlwt.Workbook(encoding="utf-8",style_compression=0)
sheet = wb.add_sheet("动漫之家",cell_overwrite_ok=True)
sheet.write(0,0,"序号")
sheet.write(0,1,"名称")
sheet.write(0,2,"链接")
n = 1

url = "https://www.dmzj.com/info/benghuai3rd.html"
browser = webdriver.Chrome(ChromeDriverManager().install())
# 访问网页
browser.get(url)
# 获取页面内容
html_content = browser.page_source
# 解析HTML内容
soup = BeautifulSoup(html_content, 'html.parser')
# print(soup)
time.sleep(2)

item = soup.find(class_="list_con_li autoHeight").find_all("a")

for i in item:
    # print(i,end="_"*50)
    link_tag = i["href"]

    # item_link = i.get("href")
    link = "https://www.dmzj.com"+link_tag
    # 获取链接值
    chapter_title = i.text
    print(chapter_title)

    sheet.write(n,0,n)
    sheet.write(n,1,chapter_title)
    sheet.write(n,2,link)
    n += 1
    wb.save("动漫之家.xls")




