import json


class MockResponse:

    def __init__(self, data):
        self.data = data

    # mock json() method always returns a specific testing dictionary
    # @staticmethod
    def json(self):
        return json.loads(self.data)
