from datetime import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

import json

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# url = "https://www.amazon.com/dp/B091S7XQK9/ref=sbl_dpx_kitchen-electric-cookware_B08GC6PL3D_0?th=1"
url = "https://www.python.org/"
driver.get(url)
# price = driver.find_element(by="class name", value="a-price-whole")
# print(price.text)

# search_bar = driver.find_element(by="name", value="q")
# print(search_bar.tag_name)
#
# search_bar = driver.find_element(by="css_selector", value="q")
# print(search_bar.tag_name)

# xpath = driver.find_element(By.XPATH, """//*[@id="content"]/div/section/div[1]/div[4]/h2""")
# print(xpath.text)

events_time = driver.find_elements(By.CSS_SELECTOR, """.event-widget time""")
events_name = driver.find_elements(By.CSS_SELECTOR, """.event-widget li a""")

times = []
names = []

for i in range(len(events_name)):
    times.append({'time': events_time[i].text})
    names.append({'name': events_name[i].text})

for i in range(len(events_name)):
    times[i].update(names[i])

result = {}

for i in range(len(events_name)):
    result[i] = times[i]

print(result)

