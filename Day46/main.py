import requests
import os
from bs4 import BeautifulSoup
import pprint
import spotipy
from spotipy.oauth2 import SpotifyOAuth

date = input("enter date like YYYY-MM-DD")
URL = f"https://www.billboard.com/charts/hot-100/{date}"

response = requests.get(URL)
res = response.text

soup = BeautifulSoup(res, "html.parser")
song_names = [title.string for title in soup.findAll("h3", id="title-of-a-story", class_="c-title")]
song_names = song_names[6::4]
song_names = [title.strip() for title in song_names]


spotify = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        client_id=os.environ.get("SPOTIPY_CLIENT_ID"),
        client_secret=os.environ.get("SPOTIPY_CLIENT_SECRET"),
        redirect_uri="http://example.com",
        show_dialog=True,
        cache_path="token.txt",
        username="Ömer Faruk"
    )

)
user_id = spotify.current_user()["id"]
print(user_id)

song_uris = []
year = date.split("-")[0]
for song in song_names:
    result = spotify.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in spotify")

playlist = spotify.user_playlist_create(user=f"{user_id}", name=f"{date} Billboard 100", public=False)
spotify.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
