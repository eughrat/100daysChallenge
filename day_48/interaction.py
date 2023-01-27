

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
url = "https://en.wikipedia.org/wiki/Main_Page"
driver.get(url)

article_numbers = driver.find_element(By.XPATH, """//*[@id="articlecount"]/a[1]""")
print(article_numbers.text)
# article_numbers.click()
