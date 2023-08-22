# -*- codeing = utf-8 -*-
import datetime
import os.path
import time

import pandas as pd
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


class Stats:

    def __init__(self):
        # 从文件中加载UI定义

        # 从 UI 定义中动态 创建一个相应的窗口对象
        # 注意：里面的控件对象也成为窗口对象的属性了
        # 比如 self.ui.button , self.ui.textEdit
        self.ui = QUiLoader().load('D:/PYTHONSTUDY/ayanmi/爬虫/钛媒体/tmt.ui')

        self.ui.Button.clicked.connect(self.download)



    def download(self):
        if os.path.exists('钛媒体%s快讯.xlsx' % datetime.date.today()):
            os.remove('钛媒体%s快讯.xlsx' % datetime.date.today())
        if not os.path.isfile('钛媒体%s快讯.xlsx' % datetime.date.today()):
            df = pd.DataFrame()
            df.to_excel('钛媒体%s快讯.xlsx' % datetime.date.today(), index=False)

        page_num = 3

        def get_article_info(url):
            driver.get(url)
            pages(driver, page_num)
            save_page(driver)  # 储存数据

        def save_page(driver):
            n = 1

            soup = BeautifulSoup(driver.page_source, 'html.parser')
            articles = soup.find_all('div', class_='content_mode')
            # print(articles)
            for article in articles:
                title = article.find("span", class_="title").get_text()
                news_t = article.find("span", class_="time").get_text()
                summary = article.find("span", class_="des").get_text()
                data = {"序号": n, "标题": [news_t], "简介": [summary]}

                df = pd.read_excel('钛媒体%s快讯.xlsx' % datetime.date.today())
                data = pd.DataFrame(data)
                df = df.append(data, ignore_index=True)
                df.to_excel('钛媒体%s快讯.xlsx' % datetime.date.today(), index=False)
                n = n + 1
                print(title)
                self.ui.textEdit.append(title)

                n = n + 1
            # wb.save("钛媒体%stmt快讯.xls"%datetime.date.today())
            self.ui.textEdit.append("完成")
            driver.quit()

        def pages(driver, page_num):
            today = datetime.date.today()
            today = today.strftime('%Y-%#m-%#d')

            WebDriverWait(driver, wait_time).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "date_search_render"))
            ).click()
            WebDriverWait(driver, wait_time).until(
                EC.element_to_be_clickable((By.XPATH, "//td[@lay-ymd='%s']" % today))
            ).click()
            WebDriverWait(driver, wait_time).until(
                EC.element_to_be_clickable((By.XPATH, "//td[@lay-ymd='%s']" % today))
            ).click()

            WebDriverWait(driver, wait_time).until(
                EC.element_to_be_clickable((By.XPATH, '//span[@lay-type="confirm"]'))).click()

            while True:
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")  # 滚动到底
                time.sleep(2)  # 等待页面加载

                try:
                    element = driver.find_element_by_xpath("//p[text()='没有相关内容']")
                    print("爬取完成，正在下载")
                    self.ui.textEdit.append("爬取完成，正在下载")
                    break
                except:
                    pass
            return driver

        if __name__ == "__main__":
            try:
                chrome_options = webdriver.ChromeOptions()
                chrome_options.add_argument("--window-size=1920,1080")
                chrome_options.add_argument("--headless")
                driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
                wait_time = 10
                url = 'https://www.tmtpost.com/nictation'
                get_article_info(url)

            except:
                print("请重试")
                self.ui.textEdit.append("请重试")

app = QApplication([])
stats = Stats()
stats.ui.show()
app.exec_()
