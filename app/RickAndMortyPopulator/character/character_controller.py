from flask import request, Blueprint
from app.RickAndMortyPopulator.character.character_service import RickAndMortyService
from app.RickAndMortyPopulator.character.character_client import RickAndMortyClient


character_page = Blueprint('character_page', __name__)

@character_page.route('/character')
def rickandmorty_service():
    return RickAndMortyService.data_character(RickAndMortyClient.base_url(), RickAndMortyClient.end_point_character())

