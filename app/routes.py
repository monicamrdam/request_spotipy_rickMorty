from flask import request
from app import app
from flask import jsonify
from app.RickAndMortyPopulator.all_character.all_character_service import AllRickAndMortyService
from app.RickAndMortyPopulator.character.rick_and_morty_client import RickAndMortyClient


@app.route('/')
def home():
    message = {
        "Home": 'http://127.0.0.1:3000/',
        "Artist": 'http://127.0.0.1:3000/artist?name=',
        "Character": 'http://127.0.0.1:3000/character',
        "AllCharacter": 'http://127.0.0.1:3000/all_character',
        "Episode": 'http://127.0.0.1:3000/episode',
        "Favourites": 'http://127.0.0.1:3000/favourites',

    }
    return jsonify(message)


@app.route('/episode')
def rickandmorty_service_episodes():
    return AllRickAndMortyService.data_episode(RickAndMortyClient.base_url(), RickAndMortyClient.end_point_episode(),
                                               AllRickAndMortyService.num_page_episode())
