import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os

os.environ['SPOTIPY_CLIENT_ID'] = 'f57033e4039647999c11f6bd7b026af8'
os.environ['SPOTIPY_CLIENT_SECRET'] = '339191ccaa2f4f7eb450a8ff4aabc04c'

# sets up spotify API client
spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

# insert the spotify playlist ID here and the username of the account
spotify_playlist_id = '72yaYysCp8xkoxwc639Sj0'
username = 'drypdrop'

# gets each track from the playlist
results = spotify.playlist_tracks(spotify_playlist_id)
tracks = results['items']

playlist = spotify.user_playlist(username, spotify_playlist_id)
playlist_name = playlist['name']
print(f"Playlist name: {playlist_name}")

while results['next']:
    results = spotify.next(results)
    tracks.extend(results['items'])

# youtube api stuff
import os
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
from google.oauth2.credentials import Credentials

# Set up the OAuth credentials
scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]
os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
os.environ['YOUTUBE_CLIENT_ID'] = '301957924875-udcdh5disglkf3nmobjga0q3oqso49av.apps.googleusercontent.com'
os.environ['YOUTUBE_CLIENT_SECRET'] = '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'

# Create flow object and check for saved credentials
flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
    "/College/Year 2022-2023/cs projects/Uski/client_secret.json", scopes
)
creds = None

# if token is not found, user is prompted to provide authorization
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
youtube_playlist_id = response['id']

# Add songs to the playlist
for track in tracks:
    # Search for the song on YouTube
    query = f"{track['track']['name']} {track['track']['artists'][0]['name']} official video"
    try:
        search_response = youtube.search().list(
            q=query,
            part="id",
            maxResults=1,
            type="video"
        ).execute()

# Extract the video ID from the search response
        video_id = search_response['items'][0]['id']['videoId']
        request_body = {
            "snippet": {
                "playlistId": youtube_playlist_id,
                "resourceId": {
                    "kind": "youtube#video",
                    "videoId": video_id
                }
            }
        }
        youtube.playlistItems().insert(
            part="snippet",
            body=request_body
        ).execute()
    except Exception as e:
        print(f"Error adding song {track['track']['name']} to playlist: {e}")