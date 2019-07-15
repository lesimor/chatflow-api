# Code by ByungWook.Kang @lesimor
from typing import List
from konlpy.tag import Okt

okt = Okt()
okt.pos('안녕하세요. 반갑습니다.', norm=True, stem=True)


class Domain:
    def __init__(self, sentence: str):
        self._sentence = sentence

    def match(self) -> bool:
        pass

    @property
    def morphs(self) -> List[tuple]:
        return okt.pos(self._sentence, norm=True, stem=True)

    @classmethod
    def analyze_utterance(cls, utterance) -> dict:
        return {
            'phrases': okt.phrases(utterance),
            'nouns': okt.nouns(utterance),
            'pos': [{'norm': norm[0], 'stem': stem[0], 'pos': norm[1]} for norm, stem in
                    zip(okt.pos(utterance, norm=True), okt.pos(utterance, norm=True, stem=True))],
            'morphs': okt.morphs(utterance)
        }
