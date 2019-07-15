# Code by ByungWook.Kang @lesimor
import json

from django.http import HttpResponse, JsonResponse
from django.views import View

from domains import Domain
from utils.response import Response


class DomainView(View):

    def post(self, request, *args, **kwargs):
        try:
            # Get payload from request
            body_unicode = request.body.decode('utf-8')
            body = json.loads(body_unicode)
            utterance = body.get('utterance')

            data = Domain.analyze_utterance(utterance)
            res = Response(data)
            return JsonResponse(res.response, json_dumps_params={'ensure_ascii': True})
        except:
            # TODO: Error handling
            return HttpResponse('Error occurred!')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
