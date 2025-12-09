from dotenv import load_dotenv
from uri import spotify_uris
load_dotenv()
import os
import spotipy
def create_playlist():
    song_uris, user_id, date = spotify_uris()
    from spotipy.oauth2 import SpotifyOAuth
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id = os.getenv("SPOTIFY_CLIENT_ID"),
                                                client_secret = os.getenv("SPOTIFY_CLIENT_SECRET"),
                                                redirect_uri = os.getenv("SPOTIFY_REDIRECT_URI"),
                                                scope="playlist-modify-private"))

    playlist_id = sp.user_playlist_create(user=user_id,name=f"{date[:4]}-{date[4:6]}-{date[6:]} Top 100 from Official Charts",
                                       public=False,description="Created with python")["id"]
    #Removing None values
    valid_uris = [uri for uri in song_uris if uri]
    #Adding songs to playlist
    sp.playlist_add_items(playlist_id,valid_uris)


create_playlist()