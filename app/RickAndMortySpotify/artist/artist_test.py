import unittest, requests


class TestAPI(unittest.TestCase):
    url_estopa = "http://127.0.0.1:3000/artist?name=estopa"
    url_aerosmith = "http://127.0.0.1:3000/artist?name=aerosmith"

    estopa_data = {
        "Name": "Estopa",
        "PopularTracks": [
            {
                "Name song": "Diablo",
                "Popularity": 68
            },
            {
                "Name song": "Como Camar\u00f3n",
                "Popularity": 68
            },
            {
                "Name song": "Tu Calorro",
                "Popularity": 67
            },
            {
                "Name song": "Ay Haiti!",
                "Popularity": 65
            },
            {
                "Name song": "Por la Raja de Tu Falda",
                "Popularity": 65
            }
        ],
        "Popularity": 70
    }

    aerosmith_data = {
        "Name": "Aerosmith",
        "PopularTracks": [
            {
                "Name song": "Dream On",
                "Popularity": 76
            },
            {
                "Name song": "I Don't Wanna To Miss A Thing - From \"Armageddon\" Soundtrack",
                "Popularity": 65
            },
            {
                "Name song": "Crazy",
                "Popularity": 76
            },
            {
                "Name song": "Walk This Way",
                "Popularity": 63
            },
            {
                "Name song": "Cryin'",
                "Popularity": 73
            }
        ],
        "Popularity": 78
    }

    def test_estopa(self):
        resp = requests.get(self.url_estopa)
        response_json = resp.json()
        self.assertEqual(resp.status_code, 200, "Se conecta al servidor")
        self.assertEqual(response_json, self.estopa_data, "Datos de estopa")

    def test_aerosmith(self):
        resp = requests.get(self.url_aerosmith)
        response_json = resp.json()
        self.assertEqual(resp.status_code, 200, "Se conecta al servidor")
        self.assertEqual(response_json, self.aerosmith_data, "Datos de Aerosmith")


if __name__ == "__main__":
    tester = TestAPI()
    tester.test_estopa()
    tester.test_aerosmith()
