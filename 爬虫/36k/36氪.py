# -*- codeing = utf-8 -*-
import time

import xlwt
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

wb = xlwt.Workbook(encoding="utf-8",style_compression=0)
sheet = wb.add_sheet("b站爬去",cell_overwrite_ok=True)
sheet.write(0,0,"序号")
sheet.write(0,1,"名称")
sheet.write(0,2,"链接")
sheet.write(0,3,"观看次数")

def get_article_info(url):
    driver.get(url)

    time.sleep(2)  # 等待页面加载
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") #滚动到底
    time.sleep(2)  # 等待页面加载
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")  # 滚动到底
    time.sleep(2)  # 等待页面加载
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    articles = soup.find_all('div', class_='kr-shadow-content')
    n = 1
    for article in articles:

        title = article.find("a",class_="article-item-title").get_text()
        link = "https://www.36kr.com" + article.find("a")['href']
        summary = article.find("a",class_="article-item-description ellipsis-2").get_text()

        sheet.write(n, 0, n)
        sheet.write(n, 1, title)
        sheet.write(n, 2, link)
        sheet.write(n, 3, summary)
        n = n + 1
    wb.save("36k_news.xls")
        # print(f"标题：{title}")
        # print(f"链接：{link}")
        # print(f"概述：{summary}\n")
    # for i in range(1,3):
    #     next_page = driver.find_element_by_xpath("//*[@id='app']/div/div[2]/div[3]/div/div/div[2]/div[2]/div[2]")
    #     next_page.click()
    #     title = article.find("a", class_="article-item-title").get_text()
    #     link = "https://www.36kr.com" + article.find("a")['href']
    #     summary = article.find("a", class_="article-item-description ellipsis-2").get_text()
    #     print(title)

if __name__ == "__main__":
    # 设置WebDriver路径。确保将其替换为适用于您系统的正确路径
    # webdriver_path = "path/to/your/webdriver"
    driver = webdriver.Chrome(ChromeDriverManager().install())

    url = 'https://www.36kr.com/search/articles/mr'
    get_article_info(url)

    # while True:
        # try:
    #         # 找到“加载更多”按钮并点击
    #         driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[3]/div/div/div[2]/div[2]/div[2]")

            # time.sleep(2)  # 等待滚动
            # driver.click()
            # time.sleep(2)  # 等待新页面加载
            # get_article_info(url)
        # except Exception as e:
        #     print("没有更多文章了")
        #     break

    # driver.quit()