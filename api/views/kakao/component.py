# Code by ByungWook.Kang @lesimor
from utils.dictionary_container import DictionaryContainer


class Component(DictionaryContainer):
    KEY = 'COMPONENT'

    def __init__(self):
        super().__init__({})

    def to_dict(self):
        return {
            self.KEY: super().to_dict()
        }


class SimpleText(Component):
    KEY = 'simpleText'

    def __init__(self, text):
        super().__init__()
        self.set('text', text)
