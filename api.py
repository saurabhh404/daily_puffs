import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

c_id = os.getenv("SPOTIFY_CLIENT_ID", "")
c_secret = os.getenv("SPOTIFY_CLIENT_SECRET", "")
client_credentials = SpotifyClientCredentials(client_id=c_id, client_secret=c_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials)

playlist_link = os.getenv("SPOTIFY_PLAYLIST_LINK", "")
playlist_uri = playlist_link.split("/")[-1].split("?")[0]
track_uris = [x["track"]["uri"] for x in sp.playlist_tracks(playlist_uri)["items"]]
print(sp.audio_features(track_uris))
