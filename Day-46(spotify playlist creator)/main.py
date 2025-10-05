
import os
import dotenv
import requests
import re
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from bs4 import BeautifulSoup
from datetime import *

dotenv.load_dotenv()
user_choice = input("From which date do you want to scrape the data? (write date in format YYYY-MM- or write 'now')': ")
if user_choice == "now":
    date = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")
else:
    date = datetime.strptime(user_choice, "%Y-%m-%d")

# -------------------Data scraping ----------------
response = requests.get(f"https://www.billboard.com/charts/hot-100{date}")
response.raise_for_status()

content = response.text

soup = BeautifulSoup(content, "html.parser")
titles = soup.select("li.o-chart-results-list__item h3#title-of-a-story")
artists = soup.select("li.o-chart-results-list__item span.c-label.a-no-trucate.u-font-size-15")

tracks = {}

for i in range(len(titles)) :
    title = titles[i]
    artist = artists[i]
    title_text = re.sub(r"[\n\t\r]","",title.text)
    artist_text = re.sub(r"[\n\t\r]","",artist.text)
    print(title_text, "-", artist_text)
    tracks[title_text] = artist_text


# -------------------Spotify ------------------

scope = "playlist-modify-public user-read-private"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

user_id = sp.current_user()['id']

playlist = sp.user_playlist_create(
    user=user_id,
    name=f"Top - 100 Bilboard tracks from {date}",
    public=True,
    description="Playlista stworzona przez Spotipy - zawiera top 100 utworów z bilboardu"
)

to_add = []
for title, artist in tracks.items():
    query = f"{title} {artist}"
    response = sp.search(query, limit=1, type="track")
    track = response["tracks"]["items"][0]

    if track:
        track_id = track["id"]
        to_add.append(track_id)
        print(f"Added {title} - {artist}")
    else:
        print(f"Couldn't find {title} - {artist}")

if to_add:
    sp.playlist_add_items(playlist_id=playlist["id"], items=to_add)
    print("Playlist updated!")
else:
    print("No tracks to add!")

