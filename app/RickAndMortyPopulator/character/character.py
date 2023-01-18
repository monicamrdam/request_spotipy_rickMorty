class Character:
    def __init__(self, uuid, name, location, episode: []):
        self.uuid = uuid
        self.name = name
        self.location = location
        self.episode = episode

    def __str__(self):
        return "Uuid {},Name {}, Location {}, Episode {}".format(
            self.uuid, self.name, self.location, self.episode
        )

    def serialize(self):
        return {
            'Uuid': self.uuid,
            'Name': self.name,
            'Location': self.location,
            'Episode': self.episode,
        }
