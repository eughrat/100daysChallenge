from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth



SPOTIFY_CLIENT_ID = '88a35b83411249aab944a0feb6672b60'
SPOTIFY_CLIENT_SECRET = "a2797095e34a48abb4968f4575dfd2a2"


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

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://mysite.com/callback/ ",
        client_id=SPOTIFY_CLIENT_ID,
        client_secret=SPOTIFY_CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]