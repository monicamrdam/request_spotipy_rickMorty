from app.artist.spotify_client import SpotifyClient
from app.artist.artist import Artist


class SpotifyService:
    def __init__(self):
        pass

    @staticmethod
    def get_artist_popularity(name_artist):
        datos_artista={}
        datos = SpotifyClient.authorization(name_artist)
        artista=Artist(datos['name'], datos['popularity'])
        datos_artista={
            'name': artista.name,
            'popularity':artista.popularity
        }
        return datos_artista