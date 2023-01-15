
from flask import request, Blueprint
from app.RickAndMortyPopulator.character.rick_and_morty_client import RickAndMortyClient


episode_page = Blueprint('episode_page', __name__)

@episode_page.route('/episode')
def rickandmorty_service():
    return AllRickAndMortyService.data_episode(RickAndMortyClient.base_url(), RickAndMortyClient.end_point_episode(),
                                               AllRickAndMortyService.num_page_episode())