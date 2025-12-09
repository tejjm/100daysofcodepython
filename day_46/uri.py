from dotenv import load_dotenv
from scrapper import songs_scrapper
load_dotenv()
import os
import spotipy
def spotify_uris():
    from spotipy.oauth2 import SpotifyOAuth
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id = os.getenv("SPOTIFY_CLIENT_ID"),
                                                client_secret = os.getenv("SPOTIFY_CLIENT_SECRET"),
                                                redirect_uri = os.getenv("SPOTIFY_REDIRECT_URI"),
                                                scope="playlist-modify-private"))
    user_id = sp.current_user()["id"]
    songs,full_titles,date=songs_scrapper()
    song_uris = []
    for song in songs:
        result = sp.search(q=f"track:{song} year:{date[:4]}",type="track",limit=1)
        track = result["tracks"]["items"]
        if track:
            uri = track[0]["uri"]
        else:
            uri = None
        print(uri)
        song_uris.append(uri)
    return song_uris, user_id, date