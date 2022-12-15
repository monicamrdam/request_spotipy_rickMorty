import requests
from config import Config
class SpotifyClient:

    def __init__(self):
        pass

    @staticmethod
    def authorization(name_artist):
        client_id = Config.CLIENT_ID
        client_secret = Config.CLIENTE_SECRET

        auth_url = 'https://accounts.spotify.com/api/token'
        data = {
            'grant_type': 'client_credentials',
            'client_id': client_id,
            'client_secret': client_secret,
        }
        auth_response = requests.post(auth_url, data=data)
        access_token = auth_response.json().get('access_token')
        headers = {
            'Authorization': 'Bearer {}'.format(access_token)
        }

        base_url = Config.URL_Search
        name=str(name_artist)
        featured_playlists_endpoint = '?q='+ name +'&type=artist'
        featured_playlists_url = ''.join([base_url, featured_playlists_endpoint])
        print (featured_playlists_url)
        response = requests.get(featured_playlists_url, headers=headers)
        id_artist=response.json()['artists']['items'][0]['id']

        print(id_artist)
        base_url_artist = Config.URL_Artist
        featured_playlists_endpoint = '/'+ id_artist
        featured_playlists_url_artist = ''.join([base_url_artist, featured_playlists_endpoint])
        print(featured_playlists_url_artist)
        response_artist = requests.get(featured_playlists_url_artist, headers=headers)


        return response_artist.json()