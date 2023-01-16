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

title_tags = soup.find_all(class_="titleline")
score_tags = soup.find_all(class_="score")
link_tags = soup.find_all(class_="sitestr")

print(len(title_tags))
print(len(score_tags))
print(len(link_tags))

titles = []
scores = []
links = []

for i in range(len(title_tags)):
    try:
        title = title_tags[i].get_text()
        titles.append(title)
        # print(title_tags[i].get_text())
        score = score_tags[i].get_text()
        scores.append(score)
        # print(score_tags[i].get_text())
        link = link_tags[i].get_text()
        links.append(link)
        # print(link_tags[i].get_text())
    except IndexError:
        continue

for i in range(len(scores)):
    points = scores[i].split(" ")
    scores[i] = int(points[0])

highest_score_idx = scores.index(max(scores))
print(titles[highest_score_idx])
print(links[highest_score_idx])


print(titles)
print(scores)
print(links)


# for tag in title_tags:
#     print(tag.get_text())
#     print(tag.get("href"))



