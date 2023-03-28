import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os

os.environ['SPOTIPY_CLIENT_ID'] = 'f57033e4039647999c11f6bd7b026af8'
os.environ['SPOTIPY_CLIENT_SECRET'] = '339191ccaa2f4f7eb450a8ff4aabc04c'

artist_name = 'spotify:artist:36QJpDe2go2KgaRleHCDTp'

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
results = spotify.artist_top_tracks(artist_name)

playlist_id = 'S1W9pkB6FibMV7N6JhUvDfu'
username = 'drypdrop'

results = spotify.playlist_tracks(playlist_id)
tracks = results['items']
while results['next']:
    results = spotify.next(results)
    tracks.extend(results['items'])

for track in tracks:
    track_name = track['track']['name']
    artist_name = track['track']['artists'][0]['name']
    album_name = track['track']['album']['name']
    print(f"{track_name} by {artist_name} from the album {album_name}")