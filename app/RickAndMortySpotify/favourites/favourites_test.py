import unittest, requests
from config import Config


class TestAPI(unittest.TestCase):
    url_favourites = Config.URL_PORT + "favourites"

    favourites_data = [
        {
            "name": "Rick Sanchez",
            "popularTracks": [
                {
                    "name": "Move Ya Feet",
                    "popularity": 12
                },
                {
                    "name": "New To The Game",
                    "popularity": 7
                },
                {
                    "name": "Freaky",
                    "popularity": 2
                },
                {
                    "name": "Move Ya Feet - Club Mix",
                    "popularity": 1
                },
                {
                    "name": "Where?",
                    "popularity": 1
                }
            ],
            "popularity": 3
        },
        [],
        {
            "name": "Summer Smith",
            "popularTracks": [
                {
                    "name": "Ring",
                    "popularity": 0
                },
                {
                    "name": "Dirty Sexy Money",
                    "popularity": 0
                },
                {
                    "name": "What If",
                    "popularity": 0
                },
                {
                    "name": "Without You",
                    "popularity": 0
                },
                {
                    "name": "Sun in Our Eyes",
                    "popularity": 0
                }
            ],
            "popularity": 0
        },
        [],
        {
            "name": "Jerry Smith",
            "popularTracks": [
                {
                    "name": "Bumbum granada",
                    "popularity": 64
                },
                {
                    "name": "Papai da Revoada - Ao Vivo",
                    "popularity": 63
                },
                {
                    "name": "Quem Me Dera",
                    "popularity": 61
                },
                {
                    "name": "Pode Se Soltar",
                    "popularity": 55
                },
                {
                    "name": "Trof\u00e9u do Ano",
                    "popularity": 54
                }
            ],
            "popularity": 58
        },
        [],
        {
            "name": "Abraham Licorne",
            "popularTracks": [
                {
                    "name": "Red Light",
                    "popularity": 25
                },
                {
                    "name": "Good Life to You - Abraham Licorne Remix",
                    "popularity": 0
                },
                {
                    "name": "Balkan Move - Original",
                    "popularity": 0
                },
                {
                    "name": "Stardust",
                    "popularity": 0
                },
                {
                    "name": "The Beginning - Original Mix",
                    "popularity": 0
                }
            ],
            "popularity": 9
        },
        {
            "name": "JUDGE",
            "popularTracks": [
                {
                    "name": "Serial Killer",
                    "popularity": 58
                },
                {
                    "name": "blood (feat. KennyHoopla & JUDGE)",
                    "popularity": 54
                },
                {
                    "name": "Heart to Break - JUDGE Remix",
                    "popularity": 19
                },
                {
                    "name": "Don't Forget Us",
                    "popularity": 12
                },
                {
                    "name": "I'm OK (feat. Shaylen) - JUDGE Remix",
                    "popularity": 12
                }
            ],
            "popularity": 43
        },
        {
            "name": "Agency",
            "popularTracks": [
                {
                    "name": "Misfit",
                    "popularity": 31
                },
                {
                    "name": "SING",
                    "popularity": 22
                },
                {
                    "name": "Baby I Want Your Love - CASSIMM Remix",
                    "popularity": 10
                },
                {
                    "name": "Dream",
                    "popularity": 6
                },
                {
                    "name": "Everybody's Got To Learn Sometime",
                    "popularity": 6
                }
            ],
            "popularity": 17
        },
        {
            "name": "Allan Rayman",
            "popularTracks": [
                {
                    "name": "Word Of Mouth",
                    "popularity": 54
                },
                {
                    "name": "Pretty Bug (feat. James Vincent McMorrow)",
                    "popularity": 52
                },
                {
                    "name": "Fish Called Happy",
                    "popularity": 52
                },
                {
                    "name": "Tennessee",
                    "popularity": 51
                },
                {
                    "name": "Lucy The Tease",
                    "popularity": 51
                }
            ],
            "popularity": 53
        },
        {
            "name": "Albert Einstein",
            "popularTracks": [
                {
                    "name": "Cap\u00edtulo 1.2 - 500 citas para estimular la creatividad",
                    "popularity": 5
                },
                {
                    "name": "Albert Einstein - Mein Weltbild, Kapitel 1.1 - Albert Einstein - Mein Weltbild (Ungek\u00fcrzt)",
                    "popularity": 3
                },
                {
                    "name": "E=MC2",
                    "popularity": 3
                },
                {
                    "name": "Albert Einstein - Mein Weltbild, Kapitel 1.2 & Albert Einstein - Mein Weltbild, Kapitel 2.1 - Albert Einstein - Mein Weltbild (Ungek\u00fcrzt)",
                    "popularity": 2
                },
                {
                    "name": "Albert Einstein - Mein Weltbild, Kapitel 2.2 & Albert Einstein - Mein Weltbild, Kapitel 3.1 - Albert Einstein - Mein Weltbild (Ungek\u00fcrzt)",
                    "popularity": 2
                }
            ],
            "popularity": 7
        },
        {
            "name": "Alexander 23",
            "popularTracks": [
                {
                    "name": "IDK You Yet",
                    "popularity": 78
                },
                {
                    "name": "Cry Over Boys",
                    "popularity": 61
                },
                {
                    "name": "The Hardest Part",
                    "popularity": 60
                },
                {
                    "name": "Ain't Christmas (with Laufey)",
                    "popularity": 58
                },
                {
                    "name": "Hate Me If It Helps",
                    "popularity": 56
                }
            ],
            "popularity": 64
        },
        {
            "name": "Alien Family",
            "popularTracks": [
                {
                    "name": "Alien Fam",
                    "popularity": 33
                },
                {
                    "name": "Cups of Coffee",
                    "popularity": 29
                },
                {
                    "name": "All I Get",
                    "popularity": 21
                },
                {
                    "name": "Shot Collar",
                    "popularity": 20
                },
                {
                    "name": "Los Angeles",
                    "popularity": 18
                }
            ],
            "popularity": 21
        },
        {
            "name": "Alien Nosejob",
            "popularTracks": [
                {
                    "name": "Television Sets",
                    "popularity": 48
                },
                {
                    "name": "Emotional Rep",
                    "popularity": 39
                },
                {
                    "name": "Freezing Cold",
                    "popularity": 38
                },
                {
                    "name": "Black Sheep",
                    "popularity": 37
                },
                {
                    "name": "Rainbow Road",
                    "popularity": 34
                }
            ],
            "popularity": 37
        },
        [],
        {
            "name": "Amish Kumar",
            "popularTracks": [
                {
                    "name": "The Tidying Song",
                    "popularity": 42
                },
                {
                    "name": "Kavithe Kavithe",
                    "popularity": 12
                },
                {
                    "name": "Nannolage Naanilla",
                    "popularity": 0
                },
                {
                    "name": "Rangia Mane",
                    "popularity": 0
                },
                {
                    "name": "Bannavembuva Banna",
                    "popularity": 0
                }
            ],
            "popularity": 24
        },
        {
            "name": "Annie Lennox",
            "popularTracks": [
                {
                    "name": "Sweet Dreams (Are Made of This) - Remastered",
                    "popularity": 83
                },
                {
                    "name": "Walking on Broken Glass",
                    "popularity": 68
                },
                {
                    "name": "I Put A Spell On You (Fifty Shades of Grey) - From \"Fifty Shades Of Grey\" Soundtrack",
                    "popularity": 66
                },
                {
                    "name": "Here Comes the Rain Again - Remastered Version",
                    "popularity": 65
                },
                {
                    "name": "Why",
                    "popularity": 64
                }
            ],
            "popularity": 71
        },
        {
            "name": "Antenna",
            "popularTracks": [
                {
                    "name": "Love 66",
                    "popularity": 38
                },
                {
                    "name": "Song For Udmurtia",
                    "popularity": 30
                },
                {
                    "name": "Sparks",
                    "popularity": 30
                },
                {
                    "name": "Northern Lights - Antenna Remix",
                    "popularity": 24
                },
                {
                    "name": "Astra",
                    "popularity": 20
                }
            ],
            "popularity": 25
        },
        {
            "name": "Antenna!",
            "popularTracks": [
                {
                    "name": "L'atellier",
                    "popularity": 22
                },
                {
                    "name": "Rhombus - Jazz-N-Groove Soulfuric Mix",
                    "popularity": 18
                },
                {
                    "name": "At Billie Ray's House",
                    "popularity": 13
                },
                {
                    "name": "Laguna",
                    "popularity": 12
                },
                {
                    "name": "Promises (feat. Lisa Shaw) - Antenna! Extended Remix",
                    "popularity": 6
                }
            ],
            "popularity": 12
        },
        []
    ]

    def test_favourites(self):
        resp = requests.get(self.url_favourites)
        response_json = resp.json()
        self.assertEqual(resp.status_code, 200, "Se conecta al servidor")
        self.assertEqual(response_json, self.favourites_data, "Datos de estopa")


if __name__ == "__main__":
    tester = TestAPI()
    tester.test_favourites()
