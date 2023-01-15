
from flask import request, Blueprint
from app.RickAndMortyPopulator.episode.episode_client import EpisodeClient
from app.RickAndMortyPopulator.episode.episode_service import EpisodeService


episode_page = Blueprint('episode_page', __name__)

@episode_page.route('/episode')
def rickandmorty_service():
    return EpisodeService.data_episode(EpisodeClient.base_url(), EpisodeClient.end_point_episode())