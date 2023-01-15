import random
from app.RickAndMortyPopulator.character.character_service import RickAndMortyService
from app.RickAndMortyPopulator.character.character_client import RickAndMortyClient
from app.RickAndMortySpotify.artist.artist_service import SpotifyService
from app.RickAndMortyPopulator.character.character_repository import CharacterRepository

class FavoriteSong:
    def __init__(self):
        pass

    @staticmethod
    def get_favorite_song_api():
        list_favorite = []
        response = RickAndMortyService.data_character(RickAndMortyClient.base_url(),
                                                      RickAndMortyClient.end_point_character())
        for i in response:
            list_favorite.append(SpotifyService.get_artist_popularity((i['name'])))
        return list_favorite

    @staticmethod
    def get_favorite_song_db():
        list_favorite = []

        db = CharacterRepository.get_db()
        cursor = db.cursor()
        res = cursor.execute("SELECT name FROM characters")
        all_characters = res.fetchall()
        "Return tupla"

        for i in all_characters:
            list_favorite.append(SpotifyService.get_artist_popularity(i))
        return list_favorite