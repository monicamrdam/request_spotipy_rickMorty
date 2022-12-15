from flask import request
from app import app
from flask import jsonify
from app.artist.artist_service import SpotifyService
from app.artist.spotify_client import SpotifyClient

@app.route('/')
def home():
    message={
        "Home":'http://127.0.0.1:5000/',
        "Artist": 'http://127.0.0.1:5000/artist?name=',
    }
    return jsonify(message)


@app.route('/artist')
def spotify_client():
    name= request.args.get('name', type=str)
    return SpotifyService.get_name(name)