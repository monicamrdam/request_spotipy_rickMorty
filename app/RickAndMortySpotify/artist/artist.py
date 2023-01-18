class Artist:
    def __init__(self, name: str, popularity: int, populartracks: []):
        self.name = name
        self.popularity = popularity
        self.populartracks = populartracks

    def __str__(self):
        return "Name: {}, Popularity: {}, PopularTracks{}".format(
            self.name, self.popularity, self.populartracks
        )

    def serialize(self):
        return {
            'Name': self.name,
            'Popularity': self.popularity,
            'PopularTracks': self.populartracks
        }


class TopTracks:
    def __init__(self, name_song: str, popularity: int):
        self.name_song = name_song
        self.popularity = popularity

    def __str__(self):
        return "Name song: {}, Popularity: {}".format(
            self.name_song, self.popularity
        )

    def serialize(self):
        return {
            'Name song': self.name_song,
            'Popularity': self.popularity, }
