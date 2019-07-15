# Code by ByungWook.Kang @lesimor
from utils.dictionary_container import DictionaryContainer


class SkillPayload(DictionaryContainer):
    @property
    def utterance(self):
        return self.get('userRequest.utterance')
