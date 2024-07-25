import requests
from bs4 import BeautifulSoup
from personal_info import *
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy import client
from pprint import pprint



URL = "https://www.billboard.com/charts/hot-100/"

while True:
    try:

        date = input("Which year would you like to travel to? Type the date in a YYYY-MM-DD format: ")
        break

    except:
        print("Invalid format, please try again.")

# date = "2000-08-12"

web_page = requests.get(url=f"{URL}/{date}/").text


soup = BeautifulSoup(web_page, "html.parser")
titles = soup.select(selector=" li ul li h3")

song_names = [song.getText().strip() for song in titles]


#       Getting Access Token
# spotify = spotipy.oauth2.SpotifyOAuth(client_id=SPOTIFY_CLIENT_ID, 
#                                       client_secret=SPOTIFY_CLIENT_SECRET, 
#                                       redirect_uri=URL_REDIRECT)
# access_token = spotify.get_access_token()



      #Getting User ID
spotify = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=SPOTIFY_CLIENT_ID,
        client_secret=SPOTIFY_CLIENT_SECRET,
        show_dialog=True,
        cache_path="Day-46-SpotifyPlaylist/token.txt",
        username=SPOTIFY_USERNAME, 
    )
)

user_id = spotify.current_user()["id"] #type: ignore


song_uris = []
year = date.split("-")[0]
for song in song_names:
    result = spotify.search(q=f"track:{song} year:{year}", type="track")
    # pprint(result)
    try:
        uri = result["tracks"]["items"][0]["uri"] #type: ignore
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")



#       Create Playlist

playlist = spotify.user_playlist_create(user=user_id, name=f"{date} Billboard 100 fFukurou", public=False)
print(playlist)

# Adding songs to playlist

spotify.playlist_add_items(playlist_id=playlist["id"], items=song_uris) #type: ignore
