import requests
from config import Config
class SpotifyClient:

    def __init__(self):
        pass

    @staticmethod
    def authorization():
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

        base_url = Config.URL_SPOTIFY

        headers = {
            'Authorization': 'Bearer {}'.format(access_token)
        }

        featured_playlists_endpoint = '?q=estopa&type=track'
        featured_playlists_url = ''.join([base_url, featured_playlists_endpoint])

        response = requests.get(featured_playlists_url, headers=headers)


        return response.json()['tracks']['items']