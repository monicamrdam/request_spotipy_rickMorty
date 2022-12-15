from app import app
from flask import jsonify
from app.artist.artist_service import SpotifyService
from app.artist.spotify_client import SpotifyClient

@app.route('/')
def home():
    message={
        "Home":'http://127.0.0.1:5000/',
        "Artist": 'http://127.0.0.1:5000/artist',
    }
    return jsonify(message)


@app.route('/artist')
def spotifyService():
    return SpotifyClient.authorization()