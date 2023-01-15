from app.RickAndMortyPopulator.character.character_repository import CharacterRepository
from app.RickAndMortyPopulator.episode.episode_repository import EpisodeRepository


class DbRickAndMortySpotify:

    def __init__(self):
        pass

    @staticmethod
    def create_table_characters():
        CharacterRepository.create_tables()

    @staticmethod
    def create_table_episode():
        EpisodeRepository.create_tables()
