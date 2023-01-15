class Episode:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "Name: {}".format(
            self.name
        )

    def serialize(self):
        return {
            'Name': self.name,
        }