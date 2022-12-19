import unittest
import requests


class TestAPI(unittest.TestCase):
    URL_CHARACTER = "http://127.0.0.1:5000/character"

    first_data = {
        "episode": ["Pilot", "Lawnmower Dog", "Anatomy Park", "M. Night Shaym-Aliens!", "Meeseeks and Destroy",
                    "Rick Potion #9", "Raising Gazorpazorp", "Rixty Minutes", "Something Ricked This Way Comes",
                    "Close Rick-counters of the Rick Kind", "Ricksy Business", "A Rickle in Time",
                    "Mortynight Run", "Auto Erotic Assimilation", "Total Rickall", "Get Schwifty",
                    "The Ricks Must Be Crazy", "Big Trouble in Little Sanchez",
                    "Interdimensional Cable 2: Tempting Fate", "Look Who's Purging Now",
                    "The Wedding Squanchers", "The Rickshank Rickdemption", "Rickmancing the Stone",
                    "Pickle Rick", "Vindicators 3: The Return of Worldender", "The Whirly Dirly Conspiracy",
                    "Rest and Ricklaxation", "The Ricklantis Mixup", "Morty's Mind Blowers",
                    "The ABC's of Beth", "The Rickchurian Mortydate", "Edge of Tomorty: Rick, Die, Rickpeat",
                    "The Old Man and the Seat", "One Crew Over the Crewcoo's Morty",
                    "Claw and Hoarder: Special Ricktim's Morty", "Rattlestar Ricklactica",
                    "Never Ricking Morty", "Promortyus", "The Vat of Acid Episode", "Childrick of Mort",
                    "Star Mort: Rickturn of the Jerri", "Mort Dinner Rick Andre", "Mortyplicity",
                    "A Rickconvenient Mort", "Rickdependence Spray", "Amortycan Grickfitti",
                    "Rick & Morty's Thanksploitation Spectacular", "Gotron Jerrysis Rickvangelion",
                    "Rickternal Friendshine of the Spotless Mort", "Forgetting Sarick Mortshall",
                    "Rickmurai Jack"], "id": 1, "location": "Citadel of Ricks", "name": "Rick Sanchez"}

    last_data = {"episode": ["Rixty Minutes"], "id": 20, "location": "Interdimensional Cable",
                 "name": "Ants in my Eyes Johnson"}

    def test_all_data(self):
        resp = requests.get(self.URL_CHARACTER)
        response_json = resp.json()
        self.assertEqual(resp.status_code, 200, "Se conecta al servidor")
        self.assertEqual(len(response_json), 20, "Hay 20 characters")
        self.assertEqual(response_json[0], self.first_data, "El primero es Rick")


if __name__ == "__main__":
    tester = TestAPI()
    tester.test_all_data()
