import requests
from bs4 import BeautifulSoup
import os

url = "https://mmzztt.com/photo/tag/jk/"
urls = []
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}
for i in range(1, 2):
    page_url = url + "page/" + str(i)
    response = requests.get(page_url,headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")
    # print(soup)
    image_divs = soup.find_all("a", class_="uk-inline u-thumb-v")

    # print(image_divs)
    for div in image_divs:
        # print(div)
        image_url = div["href"]
        print(image_url)
        response = requests.get(image_url, headers=headers)

        soup = BeautifulSoup(response.content, "html.parser")
        img_tags = soup.find_all("img")
        img_urls = []
        for img in img_tags:
            if img.get("height") == "240" and img.get("uk-img") == "" and img.get("width") == "360":
                img_urls.append(img)
        # print(img_tags)
        for num in img_urls:
            num_link = num['data-src']
            num_link = num_link.replace("200","960")
            print(num_link)

