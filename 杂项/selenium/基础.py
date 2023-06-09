import datetime
import time

import xlwt
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(ChromeDriverManager().install())
url = 'https://www.tmtpost.com/nictation'
driver.get(url)
time.sleep(1)
day = driver.find_element(By.CLASS_NAME,"days_label")
print(day.get_attribute("textContent"))