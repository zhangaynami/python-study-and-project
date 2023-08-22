import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
url = 'https://www.tmtpost.com/nictation'
driver.get(url)
time.sleep(1)
day = driver.find_element(By.CLASS_NAME,"days_label")
print(day.get_attribute("textContent"))