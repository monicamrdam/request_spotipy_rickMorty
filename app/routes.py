from flask import request
from app import app
from flask import jsonify
from app.artist.artist_service import SpotifyService
from app.character.character_service import RickAndMortyService

@app.route('/')
def home():
    message={
        "Home":'http://127.0.0.1:5000/',
        "Artist": 'http://127.0.0.1:5000/artist?name=',
        "Character": 'http://127.0.0.1:5000/rickandmorty',
    }
    return jsonify(message)


@app.route('/artist')
def spotify_service():
    name= request.args.get('name', type=str)
    return SpotifyService.get_artist_popularity(name)


@app.route('/rickandmorty')
def rickandmorty_service():
    return RickAndMortyService.listCharacter()