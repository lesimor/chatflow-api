# Code by ByungWook.Kang @lesimor
import json

from django.http import HttpResponse
from django.views import View

from domains import okt
from utils.response import Response


class DomainView(View):

    def post(self, request, *args, **kwargs):
        try:
            # Get payload from request
            body_unicode = request.body.decode('utf-8')
            body = json.loads(body_unicode)
            utterance = body.get('utterance')

            data = {
                'phrases': okt.phrases(utterance),
                'nouns': okt.nouns(utterance),
                'pos': {
                    'norm': okt.pos(utterance, norm=True),
                    'stem': okt.pos(utterance, norm=True, stem=True)
                },
                'morphs': okt.morphs(utterance)
            }
            res = Response(data)
            return HttpResponse(json.dumps(res.response()))
        except:
            return HttpResponse('Error occurred!')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
