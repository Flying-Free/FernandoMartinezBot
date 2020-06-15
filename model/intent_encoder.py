from json import JSONEncoder

class IntentEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__