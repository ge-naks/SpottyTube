import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os

os.environ['SPOTIPY_CLIENT_ID'] = 'f57033e4039647999c11f6bd7b026af8'
os.environ['SPOTIPY_CLIENT_SECRET'] = '339191ccaa2f4f7eb450a8ff4aabc04c'

artist_name = 'spotify:artist:36QJpDe2go2KgaRleHCDTp'

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
results = spotify.artist_top_tracks(artist_name)

playlist_id = 'spotify:playlist:013wGmqopEBhV6hPKGAgV0?si=1ada76a979aa486c'
username = 'drypdrop'

playlist = spotify.user_playlist(username, playlist_id)

playlist_name = playlist['name']
print(f"Playlist name: {playlist_name}")