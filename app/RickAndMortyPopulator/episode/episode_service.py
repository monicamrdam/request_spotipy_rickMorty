import requests
from app.RickAndMortyPopulator.episode.episode import Episode
from app.RickAndMortyPopulator.episode.episode_repository import EpisodeRepository


class EpisodeService:
    def __init__(self):
        pass

    @staticmethod
    def data_episode(baseurl, endpoint):
        path = (baseurl + endpoint)
        r = requests.get(path)
        data_episode = r.json()
        for j in data_episode['results']:
            episodes = Episode((j['name']))
            EpisodeRepository.insert_episode(EpisodeRepository.get_uuid(10), episodes.name)
        return 'Insertados datos en la tabla episodes'
