# -*- codeing = utf-8 -*-
# -*- codeing = utf-8 -*-
import datetime
import time

import xlwt
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

page_num = 3

def get_article_info(url):
    driver.get(url)
    pages(driver,page_num)
    save_page(driver) #储存数据

def save_page(driver):
    n = 1
    wb = xlwt.Workbook(encoding="utf-8", style_compression=0)
    sheet = wb.add_sheet("新闻", cell_overwrite_ok=True)
    sheet.write(0, 0, "序号")
    sheet.write(0, 1, "时间")
    sheet.write(0, 2, "标题")
    sheet.write(0, 3, "概述")


    soup = BeautifulSoup(driver.page_source, 'html.parser')
    articles = soup.find_all('div', class_='content_mode')
    # print(articles)
    for article in articles:
        title = article.find("span",class_="title").get_text()
        news_t = article.find("span",class_="time").get_text()
        summary = article.find("span",class_="des").get_text()
        print(title)
        # print(news_t)
        # print(summary)
        sheet.write(n, 0, n)
        sheet.write(n, 1, news_t)
        sheet.write(n, 2, title)
        sheet.write(n, 3, summary)

        n = n + 1
    wb.save("钛媒体%stmt快讯.xls"%datetime.date.today())

def pages(driver,page_num):
    today = datetime.date.today()
    today = today.strftime('%Y-%#m-%#d')
    # print(today)
    search =driver.find_element_by_class_name('date_search_render')
    search.click()
    time.sleep(1)
    dt = driver.find_element_by_xpath("//td[@lay-ymd='%s']"%today)
    dt.click()
    time.sleep(1)
    dt = driver.find_element_by_xpath("//td[@lay-ymd='%s']"%today)
    dt.click()
    confirm = driver.find_element_by_xpath('//span[@lay-type="confirm"]')
    confirm.click()
    i = 1
    while True:
            if i <= 25:
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")  # 滚动到底
                time.sleep(2)  # 等待页面加载
                i += 1
            else:
                break
    return driver



from selenium.webdriver.chrome.options import Options
if __name__ == "__main__":
    # chrome_options = Options()
    # chrome_options.add_argument("--headless")

    driver = webdriver.Chrome(ChromeDriverManager().install())
    url = 'https://www.tmtpost.com/nictation'
    get_article_info(url)

