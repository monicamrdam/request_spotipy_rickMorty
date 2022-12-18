import requests
from app.character.rick_and_morty_client import RickAndMortyClient
from app.character.character import Episode, Character


class RickAndMortyService:
    def __init__(self):
        pass

    @staticmethod
    def api_call():
        return RickAndMortyClient.main_path(RickAndMortyClient.base_url(), RickAndMortyClient.end_point_character())

    @staticmethod
    def num_page_character():
        num_page_character = \
            RickAndMortyClient.main_path(RickAndMortyClient.base_url(), RickAndMortyClient.end_point_character())[
                'info'][
                'pages']
        return num_page_character

    @staticmethod
    def num_page_episode():
        num_page_episode = \
            RickAndMortyClient.main_path(RickAndMortyClient.base_url(), RickAndMortyClient.end_point_episode())['info'][
                'pages']
        return num_page_episode

    @staticmethod
    def data_episode(baseurl, endpoint, num_page):
        all_episode = []
        for i in range(1, num_page + 1):
            path = (baseurl + endpoint + '?page=' + str(i))
            r = requests.get(path)
            data_episodes = r.json()
            for j in data_episodes['results']:
                episodes = Episode((['id']), (j['name']), (j['air_date']), (j['episode']), )
                episode = {
                    'id': episodes.id,
                    'name': episodes.name,
                    'air_date': episodes.air_date,
                    'episode': episodes.episode,
                }
                all_episode.append(episode)
        return all_episode

    @staticmethod
    def data_character(baseurl, endpoint, num_page):
        all_characters=[]
        for i in range(1, num_page + 1):
            path = (baseurl + endpoint + '?page=' + str(i))
            r = requests.get(path)
            data_character = r.json()
            for j in data_character['results']:
                characters = Character((j['id']),(j['name']),(j['location']['name']),(j['episode']))
                character = {
                    'id': characters.id,
                    'name': characters.name,
                    'location': characters.location,
                    'episode': characters.episode,
                }
                all_characters.append(character)
        return all_characters