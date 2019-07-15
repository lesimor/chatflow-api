# Code by ByungWook.Kang @lesimor
from utils.dictionary_container import DictionaryContainer
from api.views.kakao.component import Component
from typing import List

VERSION = 'version'
TEMPLATE = 'template'
OUTPUTS = 'outputs'


class SkillResponse(DictionaryContainer):

    def __init__(self, outputs: List[Component]):
        self.outputs = outputs
        super().__init__({
            VERSION: '2.0',
            TEMPLATE: {
                OUTPUTS: [c.to_dict() for c in self.outputs]
            }
        })
