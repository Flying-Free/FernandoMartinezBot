import json
from collections import namedtuple

from model.intent_encoder import IntentEncoder


class Intent:
    tag = None
    patterns = []
    responses = []
    context_set = None

    def __int__(self, tag, patterns, responses, context_set):
        self.tag, self.patterns, self.responses, self.context_set = tag, patterns, responses, context_set

    def __init__(self, d):
        data = json.dumps(d, indent=4, cls=IntentEncoder)
        self = json.loads(data, object_hook=self.__custom_intent_encoder)

    @staticmethod
    def __custom_intent_encoder(intentDict):
        return namedtuple('X', intentDict.keys())(*intentDict.values())
