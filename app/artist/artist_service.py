from app.artist.spotify_client import SpotifyClient


class SpotifyService:
    def __init__(self):
        pass

    @staticmethod
    def get_name(name_artist):
        return SpotifyClient.authorization(name_artist)