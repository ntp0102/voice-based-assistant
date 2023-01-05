import asyncio
from rasa.core.agent import Agent
from rasa.shared.utils.io import json_to_string


class Model:

    def __init__(self, model_path: str) -> None:
        self.agent = Agent.load(model_path)
        print("NLU model loaded")

    def message(self, message: str) -> str:
        message = message.strip()
        result = asyncio.run(
            self.agent.parse_message_using_nlu_interpreter(message))
        return result


mdl = Model("./models/nlu-20230104-170702.tar.gz")
#./models/nlu-20221218-232802.tar.gz


def chat_bot(text):
    sentence = text
    intent = mdl.message(sentence)['intent']['name']
    confidence = mdl.message(sentence)['intent']['confidence']
    if confidence < 0.75:
        return "not understand"
    return intent
