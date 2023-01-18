import unittest
import requests


class TestAPI(unittest.TestCase):
    URL_CHARACTER = "http://127.0.0.1:3000/episode"
    first_data = {"Name": "Pilot"}
    last_data_data = {"Name": "Look Who's Purging Now"}

    def episode(self):
        resp = requests.get(self.URL_CHARACTER)
        response_json = resp.json()
        self.assertEqual(resp.status_code, 200, "Se conecta al servidor")
        self.assertEqual(len(response_json), 20, "Hay 20 episode")
        self.assertEqual(response_json[0], self.first_data, "El primero es Rick")
        self.assertEqual(response_json[0], self.last_data, "El ultimo es Ants in my Eyes Johnson")


if __name__ == "__main__":
    tester = TestAPI()
    tester.episode()
