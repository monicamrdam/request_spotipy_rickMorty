import random
from app.RickAndMortyPopulator.character.character_service import RickAndMortyService
from app.RickAndMortyPopulator.character.rick_and_morty_client import RickAndMortyClient
from app.RickAndMortySpotify.artist.artist_service import SpotifyService


class FavoriteSong:
    def __init__(self):
        pass

    @staticmethod
    def get_favorite_song():
        list_favorite=[]
        response = RickAndMortyService.data_character(RickAndMortyClient.base_url(),
                                                      RickAndMortyClient.end_point_character())
        for i in response:

            list_favorite.append(SpotifyService.get_artist_popularity ((i['name'])))
        return list_favorite
