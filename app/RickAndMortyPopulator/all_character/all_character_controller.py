from flask import request, Blueprint
from app.RickAndMortyPopulator.all_character.all_character_service import AllRickAndMortyService
from app.RickAndMortyPopulator.character.rick_and_morty_client import RickAndMortyClient

all_character_page = Blueprint('all_character_page', __name__)


# SOLO USAR SI SE TIENE MUCHO TIEMPO
@all_character_page.route('/all_character')
def rickandmorty_service_characters():
    return AllRickAndMortyService.data_character(RickAndMortyClient.base_url(),
                                                 RickAndMortyClient.end_point_character(),
                                                 AllRickAndMortyService.num_page_character())
