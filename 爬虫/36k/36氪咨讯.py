# -*- codeing = utf-8 -*-
import datetime
import time
import xlwt
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

page_num = 2

def get_article_info(url):
    driver.get(url)

    time.sleep(2)  # 等待页面加载
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") #滚动到底
    time.sleep(2)  # 等待页面加载
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")  # 滚动到底
    time.sleep(2)  # 等待页面加载

    pages(driver,page_num)
    save_page(driver) #储存数据

def save_page(driver):
    n = 1
    wb = xlwt.Workbook(encoding="utf-8", style_compression=0)
    sheet = wb.add_sheet("新闻", cell_overwrite_ok=True)
    sheet.write(0, 0, "序号")
    sheet.write(0, 1, "名称")
    sheet.write(0, 2, "链接")
    sheet.write(0, 3, "观看次数")

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    articles = soup.find_all('div', class_='kr-shadow-content')

    for article in articles:
        # print(article)
        title = article.find("a",class_="article-item-title").get_text()
        link = "https://www.36kr.com" + str(article.find("a",class_="article-item-pic").get("href"))
        # link = article.find("a",class_="article-item-pic").get("href")
        # print(link)
        summary = article.find("a",class_="article-item-description ellipsis-2").get_text()

        sheet.write(n, 0, n)
        sheet.write(n, 1, title)
        sheet.write(n, 2, link)
        sheet.write(n, 3, summary)
        n = n + 1
    wb.save("36k咨询%s.xls"%datetime.date.today())
    driver.close()

def pages(driver,page_num):
    i = 1
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")  # 滚动到底
        time.sleep(2)  # 等待页面加载
        if i == page_num:
            break
        else:
            if_continue = driver.find_element_by_class_name('kr-loading-more-button')
            if if_continue.text == '查看更多':
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")  # 滚动到底
                next_page = driver.find_element_by_class_name('kr-loading-more-button')
                next_page.click()
            else:
                print("没有更多了")
        i += 1

if __name__ == "__main__":
    driver = webdriver.Chrome(ChromeDriverManager().install())
    url = 'https://www.36kr.com/information/web_news/latest'
    get_article_info(url)

