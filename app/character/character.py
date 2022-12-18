class Character:
    def __init__(self, id, name, location, episode):
        self.id = id
        self.name = name
        self.location = location
        self.episode = episode


class Episode:
    def __init__(self, name):
        self.name = name
