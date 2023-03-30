import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os

os.environ['SPOTIPY_CLIENT_ID'] = 'f57033e4039647999c11f6bd7b026af8'
os.environ['SPOTIPY_CLIENT_SECRET'] = '339191ccaa2f4f7eb450a8ff4aabc04c'

artist_name = 'spotify:artist:36QJpDe2go2KgaRleHCDTp'

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
results = spotify.artist_top_tracks(artist_name)

playlist_id = '37i9dQZF1DXcBWIGoYBM5M'
username = 'drypdrop'

results = spotify.playlist_tracks(playlist_id)
tracks = results['items']

playlist = spotify.user_playlist(username, playlist_id)
playlist_name = playlist['name']
print(f"Playlist name: {playlist_name}")

while results['next']:
    results = spotify.next(results)
    tracks.extend(results['items'])

for track in tracks:
    track_name = track['track']['name']
    artist_name = track['track']['artists'][0]['name']
    album_name = track['track']['album']['name']
    print(f"{track_name} - track - {artist_name} - artist - {album_name} - album")


# youtube api stuffz

import os
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
from google.oauth2.credentials import Credentials

# Set up the OAuth credentials
scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]
os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
os.environ['YOUTUBE_CLIENT_ID'] = '301957924875-g9vsn9741dgdnjv8ftucon2lolnjuv1e.apps.googleusercontent.com'
os.environ['YOUTUBE_CLIENT_SECRET'] = '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'

# Create flow object and check for saved credentials
flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
    "/College/Year 2022-2023/cs projects/Uski/client_secret.json", scopes
)
creds = None
if os.path.exists('token.json'):
    creds = Credentials.from_authorized_user_file('token.json', scopes)
else:
    creds = flow.run_local_server(port=8080, prompt='consent', authorization_prompt_message='')

    # Save the credentials for the next run
    with open('token.json', 'w') as token:
        token.write(creds.to_json())

# Set up the YouTube Data API client
youtube = googleapiclient.discovery.build("youtube", "v3", credentials=creds)

# Create a new playlist
playlist_title = "Uski Test Playlist"
request_body = {
    "snippet": {
        "title": playlist_title,
        "description": "New playlist created using Uski"
    },
    "status": {
        "privacyStatus": "public"
    }
}

response = youtube.playlists().insert(
    part="snippet,status",
    body=request_body
).execute()

# Get the ID of the new playlist
playlist_id = response['id']

# Add a video to the playlist
video_id = "vtZtb9Ji_9A"

request_body = {
    "snippet": {
        "playlistId": playlist_id,
        "resourceId": {
            "kind": "youtube#video",
            "videoId": video_id
        }
    }
}

response = youtube.playlistItems().insert(
    part="snippet",
    body=request_body
).execute()

# Print the response to confirm that the video was added to the playlist
 # print(response)

 # hiding response rn cuz it shows in terminal, remove comment if you wanna see in terminal ^^^