from app import app
from flask import jsonify


@app.route('/')
def home():
    message = {
        "Home": 'http://127.0.0.1:3000/',
        "Artist": 'http://127.0.0.1:3000/artist?name=',
        "Character": 'http://127.0.0.1:3000/character',
        "Episode": 'http://127.0.0.1:3000/episode',
        "Favourites": 'http://127.0.0.1:3000/favourites',

    }
    return jsonify(message)
