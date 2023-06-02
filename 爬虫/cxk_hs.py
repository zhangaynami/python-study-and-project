# -*- codeing = utf-8 -*-
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time
from bs4 import BeautifulSoup
#打开B站
def search(url="https://www.bilibili.com/"):
    try:
        # browser = webdriver.Chrome(ChromeDriverManager().install())
        # browser.set_window_size(1400, 900)
        chrome_options = Options()
        chrome_options.add_argument('--headless')#请求无头游览器
        browser = webdriver.Chrome(ChromeDriverManager().install(),chrome_options=chrome_options)
        browser.get(url)
        first_page = browser.find_element_by_xpath("//*[@id='i_cecream']/div[2]/div[1]/div[1]/ul[1]/li[1]/a/span")
        first_page.click()
        input = browser.find_element_by_xpath("//*[@id='nav-searchform']/div[1]/input")
        input.send_keys('蔡徐坤 篮球')
        submit = browser.find_element_by_xpath("//*[@id='nav-searchform']/div[2]")
        submit.click()
        all_h = browser.window_handles
        browser.switch_to.window(all_h[1])
        return browser
    except TimeoutError:
        return search(url)

#存储数据
def save_to_excel(browser,sheet,n,wb):
    try:
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
            print(item_title)

            sheet.write(n, 0, n)
            sheet.write(n, 1, item_title)
            sheet.write(n, 2, item_link)
            sheet.write(n, 3, item_readers)
            sheet.write(n, 4, item_danmu)
            sheet.write(n, 5, item_time)
            sheet.write(n, 6, item_author)
            n += 1
        wb.save("cxk1.xls")
        print(n)
        return n
    except TimeoutError:
        save_to_excel(browser,sheet,n,wb) #c出出汗书存储函数

#翻页函数
def next_page(browser): #获取下一页
    try:
        next = browser.find_element_by_xpath("//button[text()='下一页']") #下一页按钮
        next.click()
        time.sleep(1)
        all_h1 = browser.window_handles
        browser.switch_to.window(all_h1[1]) #定位到当前页面
        return browser
    except:
        next_page(browser)


