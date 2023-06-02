# -*- codeing = utf-8 -*-
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup
import xlwt

wb = xlwt.Workbook(encoding="utf-8",style_compression=0)
sheet = wb.add_sheet("b站爬去",cell_overwrite_ok=True)
sheet.write(0,0,"序号")
sheet.write(0,1,"名称")
sheet.write(0,2,"链接")
sheet.write(0,3,"观看次数")
sheet.write(0,4,"弹幕")
sheet.write(0,5,"时间")
sheet.write(0,6,"作者")

n = 1
browser = webdriver.Chrome(ChromeDriverManager().install())
WAIT = WebDriverWait(browser,10)
browser.set_window_size(1400,900)
browser.get("https://www.bilibili.com/")
first_page = browser.find_element_by_xpath("//*[@id='i_cecream']/div[2]/div[1]/div[1]/ul[1]/li[1]/a/span")
first_page.click()
input = browser.find_element_by_xpath("//*[@id='nav-searchform']/div[1]/input")
input.send_keys('蔡徐坤 篮球')
submit = browser.find_element_by_xpath("//*[@id='nav-searchform']/div[2]")
submit.click()
all_h = browser.window_handles
browser.switch_to.window(all_h[1])
html = browser.page_source
soup = BeautifulSoup(html,"lxml")
videos = soup.find(class_='video-list').find_all(class_='bili-video-card')
# print(videos)
for item in videos:
    item_readers = item.find("span",class_="bili-video-card__stats--item").span.string
    item_danmu = item.find_all("span",class_="bili-video-card__stats--item")[1].span.string
    item_time = item.find("span",class_="bili-video-card__stats__duration").string
    item_title = item.find("h3").get("title")
    item_author = item.find("span", class_="bili-video-card__info--author").string
    item_link = item.find("a").get("href")[2:]


    sheet.write(n,0,n)
    sheet.write(n,1,item_title)
    sheet.write(n,2,item_link)
    sheet.write(n,3,item_readers)
    sheet.write(n,4,item_danmu)
    sheet.write(n,5,item_time)
    sheet.write(n,6,item_author)

    print(item_title)
    # print(item_link)
    # print(item_time)
    # print(item_danmu)
    # print(item_readers)
    n += 1

all_h = browser.window_handles
browser.switch_to.window(all_h[1])

total = browser.find_element_by_xpath("//*[@id='i_cecream']/div/div[2]/div[2]/div/div/div/div[2]/div/div/button[9]").text
next = browser.find_element_by_xpath("//button[@class='vui_button vui_pagenation--btn vui_pagenation--btn-side']")
next.click()
time.sleep(1)
all_h1 = browser.window_handles
browser.switch_to.window(all_h1[1])
html = browser.page_source
soup = BeautifulSoup(html,"lxml")
videos = soup.find(class_='video-list').find_all(class_='bili-video-card')
for item in videos:
    item_readers = item.find("span",class_="bili-video-card__stats--item").span.string
    item_danmu = item.find_all("span",class_="bili-video-card__stats--item")[1].span.string
    item_time = item.find("span",class_="bili-video-card__stats__duration").string
    item_title = item.find("h3").get("title")
    item_author = item.find("span", class_="bili-video-card__info--author").string
    item_link = item.find("a").get("href")[2:]
    sheet.write(n,0,n)
    sheet.write(n,1,item_title)
    sheet.write(n,2,item_link)
    sheet.write(n,3,item_readers)
    sheet.write(n,4,item_danmu)
    sheet.write(n,5,item_time)
    sheet.write(n,6,item_author)
    n += 1
wb.save("cxk.xls")
for i in range(3,int(total)+1):
    time.sleep(2)
    next1 = browser.find_element_by_xpath("//*[@id='i_cecream']/div/div[2]/div[2]/div/div/div[2]/div/div/button[10]")
    next1.click()
    time.sleep(1)
    all_h2 = browser.window_handles
    browser.switch_to.window(all_h2[1])
    html = browser.page_source
    soup = BeautifulSoup(html, "lxml")
    videos = soup.find(class_='video-list').find_all(class_='bili-video-card')
    for item in videos:
        item_readers = item.find("span", class_="bili-video-card__stats--item").span.string
        item_danmu = item.find_all("span", class_="bili-video-card__stats--item")[1].span.string
        item_time = item.find("span", class_="bili-video-card__stats__duration").string
        item_title = item.find("h3").get("title")
        item_author = item.find("span", class_="bili-video-card__info--author").string
        item_link = item.find("a").get("href")[2:]

        sheet.write(n, 0, n)
        sheet.write(n, 1, item_title)
        sheet.write(n, 2, item_link)
        sheet.write(n, 3, item_readers)
        sheet.write(n, 4, item_danmu)
        sheet.write(n, 5, item_time)
        sheet.write(n, 6, item_author)
        n += 1
        wb.save("cxk1.xls")
