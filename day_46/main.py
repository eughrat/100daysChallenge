from bs4 import BeautifulSoup
import requests




year_to_travel = input("Which year do you want to travel to? Type the date in this formaat YYYY-MM-DD: ")

response = requests.get(f"https://www.billboard.com/charts/hot-100/{year_to_travel}/")
web_page = response.text

soup = BeautifulSoup(web_page, "html.parser")
print(soup.title)

title_tags = soup.select(selector='li #title-of-a-story')
titles = []

for i in range(len(title_tags)):
    try:
        title = title_tags[i].get_text().replace("\n", "").replace("\t","")
        titles.append(title)
    except IndexError:
        continue

print(titles)