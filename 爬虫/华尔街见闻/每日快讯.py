# -*- codeing = utf-8 -*-
import datetime
import os.path
import time

import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

if os.path.exists('华尔街见闻%s快讯.xlsx'%datetime.date.today()):
    os.remove('华尔街见闻%s快讯.xlsx'%datetime.date.today())
if not os.path.isfile('华尔街见闻%s快讯.xlsx'%datetime.date.today()):
    df = pd.DataFrame()
    df.to_excel('华尔街见闻%s快讯.xlsx'%datetime.date.today(), index=False)


# 清空Excel文件中的数据

def get_article_info(url):
    driver.get(url)
    pages(driver)

def save_page(driver,n):
    driver.implicitly_wait(15)
    # time.sleep(2)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    articles = soup.find_all('div',class_="live-item")


    for article in articles:

        news_t = article.find("time",class_="live-item_created").get_text()
        summary = article.find("div",class_="live-item_html").get_text()
        data = {"序号":n,"时间":[news_t],"简介":[summary]}
        print(news_t)

        df = pd.read_excel('华尔街见闻%s快讯.xlsx'%datetime.date.today())
        data = pd.DataFrame(data)
        df = df.append(data, ignore_index=True)
        df.to_excel('华尔街见闻%s快讯.xlsx'%datetime.date.today(), index=False)
        n = n + 1

def pages(driver):
    driver.implicitly_wait(15)

    search =driver.find_element_by_xpath('//span[text()="日期"]')
    search.click()
    dt = driver.find_element_by_xpath("//div[@class='day today']")
    dt.click()
    dt = driver.find_element_by_xpath("//div[@class='day today active']")
    dt.click()
    time.sleep(2)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")  # 滚动到底
  # 定位到当前页面
    # i = 1
    time.sleep(2)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    # time.sleep(2)
    max_page = int(soup.find('input',type="number").get("max"))
    n = 1
    for page_number in range(1,max_page+1):
        next_page = driver.find_element_by_xpath("//*[@id='page-livenews']/div[2]/div[2]/div[21]/div/form/input")
        next_page.clear()
        next_page.send_keys(page_number)
        time.sleep(2)
        send_page = driver.find_element_by_xpath("//button[text()='确定']")
        send_page.click()
        time.sleep(2)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")  # 滚动到底

        save_page(driver, n)
        n += 20

if __name__ == "__main__":
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(ChromeDriverManager().install(),options=chrome_options)
    #设置无头浏览器
    driver.implicitly_wait(15)
    url = 'https://wallstreetcn.com/live/global'
    get_article_info(url)
    driver.close()