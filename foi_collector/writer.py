import json

class FOISourceWriter:

    def __init__(self):
        self.data = []

    def add_data(self, data):
        self.data.append(data)

    def write(self, filename):
        with open(filename, "w") as file:
            json.dump(
                {
                    'data': self.data
                },
                file
            )
