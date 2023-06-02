# -*- codeing = utf-8 -*-
import time
import time
import requests
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import xlwt
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}

# 获取页面内容

url = "https://mmzztt.com/photo/29240"
driver = webdriver.Chrome(ChromeDriverManager().install())  # 假设使用Chrome浏览器
driver.get(url)

img_urls = []
for i in range(1,2):
    current_url = driver.current_url
    response = requests.get(current_url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")
    img_tags = soup.find_all("img")
    print(img_tags)
    img_urls = []

    # if img_tags.get("height") == "240" and img_tags.get("uk-img") == "" and img_tags.get("width") == "360":
    #     img_urls.append(img_tags)
    # for num in img_urls:
    #     num_link = num['data-src']
    #     num_link = num_link.replace("200", "960")
    #     print(num_link)
    # print(img_tags)
    next_button = driver.find_element_by_xpath("/html/body/section[1]/div/div/main/article/figure/div[3]")
    if not next_button.is_enabled():
        break
    next_button.click()
    time.sleep(1)  # 等待页面加载完成

