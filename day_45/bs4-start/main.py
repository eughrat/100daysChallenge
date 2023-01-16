# import pprint
# from bs4 import BeautifulSoup

# with open("website.html") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, 'html.parser')
#
# all_anchor_tags = soup.find_all(name="a")
#
# print(all_anchor_tags)
#
# for tag in all_anchor_tags:
#     print(tag.get("href"))
#
# heading = soup.find(name="h3", class_="heading")
# print(heading.get("class"))
#
# company_url = soup.select_one(selector="p a ")

from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
print(soup.title)

all_anchor_tags = soup.find_all(class_="titleline")

for tag in all_anchor_tags:
    print(tag.get_text())



