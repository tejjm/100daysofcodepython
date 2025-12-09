from dotenv import load_dotenv
load_dotenv()
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id = os.getenv("SPOTIFY_CLIENT_ID"),
                                            client_secret = os.getenv("SPOTIFY_CLIENT_SECRET"),
                                            redirect_uri = os.getenv("SPOTIFY_REDIRECT_URI"),
                                            scope="playlist-modify-private"))
user_id = sp.current_user()["id"]



