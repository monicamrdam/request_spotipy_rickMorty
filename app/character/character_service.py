import requests
from app.character.rick_and_morty_client import RickAndMortyClient
from app.character.character import Character


class RickAndMortyService:
    def __init__(self):
        pass


    @staticmethod
    def get_episode(list_episode_url):
        list_episode_name = []
        for episode_url in list_episode_url:
            response_body = requests.get(episode_url).json()
            episode_name = response_body['name']
            list_episode_name.append(episode_name)
        return list_episode_name

    @staticmethod
    def data_character(baseurl, endpoint):
        list_characters = []
        path = (baseurl + endpoint)
        r = requests.get(path)
        data_character = r.json()
        for j in data_character['results']:
            characters = Character((j['id']),(j['name']),(j['location']['name']),(j['episode']))
            list_episode = RickAndMortyService.get_episode(characters.episode)
            character = {
                'id': characters.id,
                'name': characters.name,
                'location': characters.location,
                'episode': list_episode,
            }
            list_characters.append(character)
        return list_characters