import random
from app.character.character_service import RickAndMortyService
from app.character.rick_and_morty_client import RickAndMortyClient
from app.artist.artist_service import SpotifyService
class FavoriteSong:
    def __init__(self):
        pass

    @staticmethod
    def get_favorite_song():
        list_name_character=[]
        response=RickAndMortyService.data_character(RickAndMortyClient.base_url(), RickAndMortyClient.end_point_character())
        for i in response:
           list_name_character.append((i['name']))
        num_list=random.randint(0, 19)
        search_name=list_name_character[num_list]
        name=''.join(search_name)
        return SpotifyService.get_artist_popularity(name)

