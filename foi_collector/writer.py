import json


class FOISourceWriter:

    def __init__(self):
        self.data = []
        self.source_title = None
        self.source_link = None

    def set_source(self, source_title=None, source_link=None):
        self.source_title = source_title
        self.source_link = source_link

    def add_data(self, data):
        self.data.append(data)

    def write(self, filename):
        with open(filename, "w") as file:
            json.dump(
                {
                    'title': self.source_title,
                    'link': self.source_link,
                    'data': self.data
                },
                file
            )
