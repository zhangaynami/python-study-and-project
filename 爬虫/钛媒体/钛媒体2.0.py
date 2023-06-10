# -*- codeing = utf-8 -*-
import datetime
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import os.path
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

if os.path.exists('钛媒体%s快讯.xlsx'%datetime.date.today()):
    os.remove('钛媒体%s快讯.xlsx'%datetime.date.today())
if not os.path.isfile('钛媒体%s快讯.xlsx'%datetime.date.today()):
    df = pd.DataFrame()
    df.to_excel('钛媒体%s快讯.xlsx'%datetime.date.today(), index=False)

page_num = 3

def get_article_info(url):
    driver.get(url)
    pages(driver,page_num)
    save_page(driver) #储存数据

def save_page(driver):
    n = 1

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    articles = soup.find_all('div', class_='content_mode')
    # print(articles)
    for article in articles:
        title = article.find("span",class_="title").get_text()
        news_t = article.find("span",class_="time").get_text()
        summary = article.find("span",class_="des").get_text()
        data = {"序号":n,"标题":[news_t],"简介":[summary]}
        print(news_t)

        df = pd.read_excel('钛媒体%s快讯.xlsx'%datetime.date.today())
        data = pd.DataFrame(data)
        df = df.append(data, ignore_index=True)
        df.to_excel('钛媒体%s快讯.xlsx'%datetime.date.today(), index=False)
        n = n + 1
        print(title)

        n = n + 1
    # wb.save("钛媒体%stmt快讯.xls"%datetime.date.today())

def pages(driver,page_num):
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
            break
        except:
            pass
    return driver

if __name__ == "__main__":
    try:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--window-size=1920,1080")
        chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(ChromeDriverManager().install(),options=chrome_options)
        wait_time =10
        url = 'https://www.tmtpost.com/nictation'
        get_article_info(url)
        driver.quit()
    except:
        print("请重试")
