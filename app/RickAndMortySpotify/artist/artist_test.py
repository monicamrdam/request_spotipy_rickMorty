import unittest, requests
from config import Config

class TestAPI(unittest.TestCase):

    url_estopa = Config.URL_PORT +"artist?name=estopa"
    url_aerosmith = Config.URL_PORT +"artist?name=aerosmith"

    estopa_data = {"name": "Estopa",
                   "popularTracks": [{"name": "Diablo", "popularity": 66},
                                     {"name": "Como Camar\u00f3n", "popularity": 67},
                                     {"name": "Tu Calorro", "popularity": 66}, {"name": "Ay Haiti!", "popularity": 64},
                                     {"name": "Vino Tinto", "popularity": 63}],
                   "popularity": 70}

    aerosmith_data = {"name": "Aerosmith", "popularTracks": [{"name": "Dream On", "popularity": 87},
                                        {"name": "I Don't Want to Miss a Thing - From \"Armageddon\" Soundtrack",
                                         "popularity": 76}, {"name": "Crazy", "popularity": 75},
                                        {"name": "Walk This Way", "popularity": 75},
                                        {"name": "Sweet Emotion", "popularity": 73}], "popularity": 77}



    def test_estopa(self):
        resp = requests.get(self.url_estopa)
        response_json = resp.json()
        self.assertEqual(resp.status_code, 200, "Se conecta al servidor")
        self.assertEqual(response_json, self.estopa_data, "Datos de estopa")


    def test_aerosmith(self):
        resp = requests.get(self.url_aerosmith)
        response_json = resp.json()
        self.assertEqual(resp.status_code, 200, "Se conecta al servidor")
        self.assertEqual(response_json[0], self.aerosmith_data, "Datos de Aerosmith")


if __name__ == "__main__":
    tester = TestAPI()
    tester.test_estopa()
    #tester.test_aerosmith()