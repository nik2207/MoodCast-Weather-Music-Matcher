# spotify_recommender.py
import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv

load_dotenv()

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id=os.getenv("SPOTIFY_CLIENT_ID"),
    client_secret=os.getenv("SPOTIFY_CLIENT_SECRET")
))

def get_recommendations(mood, weather):
    query = f"{mood} {weather} playlist"
    results = sp.search(q=query, type='playlist', limit=1)
    playlist_id = results['playlists']['items'][0]['id']

    tracks_data = sp.playlist_tracks(playlist_id)
    tracks = []
    for track in tracks_data['items'][:5]:
        track_info = track['track']
        tracks.append({
            'name': track_info['name'],
            'artists': [artist['name'] for artist in track_info['artists']],
            'url': track_info['external_urls']['spotify']
        })

    return tracks
