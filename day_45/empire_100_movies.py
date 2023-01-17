from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.imdb.com/list/ls055592025/")
empire_web_page = response.text

soup = BeautifulSoup(empire_web_page, "html.parser")
print(soup.title)

title_tags = soup.select(selector="h3 a")
titles = []


for i in range(len(title_tags)):
    try:
        title = title_tags[i].get_text()
        titles.append(title)
    except IndexError:
        continue

print(titles)

with open("movies.txt", "w", encoding='utf-8') as file:
    file.write(('\n'.join(titles)))
