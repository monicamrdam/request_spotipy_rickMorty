from flask import request
from app import app
from flask import jsonify
from app.all_character.all_character_service import AllRickAndMortyService
from app.character.character_service import RickAndMortyService
from app.character.rick_and_morty_client import RickAndMortyClient
@app.route('/')
def home():
    message = {
        "Home": 'http://127.0.0.1:5000/',
        "Artist": 'http://127.0.0.1:5000/artist?name=',
        "Character": 'http://127.0.0.1:5000/character',
        "AllCharacter": 'http://127.0.0.1:5000/all_character',
        "Episode": 'http://127.0.0.1:5000/episode',
        "Favourites": 'http://127.0.0.1:5000/favourites',

    }
    return jsonify(message)




@app.route('/character')
def rickandmorty_service():
    return RickAndMortyService.data_character(RickAndMortyClient.base_url(), RickAndMortyClient.end_point_character())



# SOLO USAR SI SE TIENE MUCHO TIEMPO
@app.route('/all_character')
def rickandmorty_service_characters():
    return AllRickAndMortyService.data_character(RickAndMortyClient.base_url(),
                                                 RickAndMortyClient.end_point_character(),
                                                 AllRickAndMortyService.num_page_character())


@app.route('/episode')
def rickandmorty_service_episodes():
    return AllRickAndMortyService.data_episode(RickAndMortyClient.base_url(), RickAndMortyClient.end_point_episode(),
                                               AllRickAndMortyService.num_page_episode())


