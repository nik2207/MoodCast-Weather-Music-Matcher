import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os
from dotenv import load_dotenv

load_dotenv()

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id=os.getenv("SPOTIFY_CLIENT_ID"),
    client_secret=os.getenv("SPOTIFY_CLIENT_SECRET")
))

def recommend_tracks(mood, weather):
    query = f"{mood} {weather}"
    results = sp.search(q=query, type='track', limit=5)
    tracks = []
    for item in results['tracks']['items']:
        tracks.append({
            'name': item['name'],
            'artist': item['artists'][0]['name'],
            'url': item['external_urls']['spotify']
        })
    return tracks
