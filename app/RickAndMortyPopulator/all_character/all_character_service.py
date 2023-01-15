import requests
import re
from app.RickAndMortyPopulator.character.rick_and_morty_client import RickAndMortyClient
from app.RickAndMortyPopulator.character.character import Episode, Character


class AllRickAndMortyService:
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
                episodes = Episode((j['name']))
                all_episode.append(episodes.name)
        return all_episode

    @staticmethod
    def search_url_episode(path_episode):
        for j in path_episode:
            tup = re.findall('[0-9]+', j)
            s = ''.join(tup)
        return s

    @staticmethod
    def search_episode(num_url):
        all_episode = AllRickAndMortyService.data_episode(RickAndMortyClient.base_url(),
                                                          RickAndMortyClient.end_point_episode(),
                                                          AllRickAndMortyService.num_page_episode())
        search_num = int(num_url)
        return all_episode[search_num - 1]

    @staticmethod
    def data_character(baseurl, endpoint, num_page):
        all_characters = []
        for i in range(1, num_page + 1):
            path = (baseurl + endpoint + '?page=' + str(i))
            r = requests.get(path)
            data_character = r.json()
            for j in data_character['results'][:1]:
                num_episode = AllRickAndMortyService.search_url_episode((j['episode']))
                name_episode = AllRickAndMortyService.search_episode(num_episode)
                # Preguntar Alberto
                # characters = Character((j['id']),(j['name']),(j['location']['name']),(j['episode']))
                characters = Character((j['id']), (j['name']), (j['location']['name']), name_episode)
                character = {
                    'id': characters.id,
                    'name': characters.name,
                    'location': characters.location,
                    'episode': characters.episode,
                }
                all_characters.append(character)
        return all_characters
