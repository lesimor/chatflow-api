# Code by ByungWook.Kang @lesimor
import json

from django.http import JsonResponse
from django.views import View

from .payload import SkillPayload
from .component import SimpleText
from .response import SkillResponse


class KakaoSkill(View):
    def post(self, request, *args, **kwargs):
        try:
            # Get payload from request
            # Generate appropriate template
            # Get payload from request
            body_unicode = request.body.decode('utf-8')
            body = json.loads(body_unicode)

            skill_payload = SkillPayload(body)
            utterance = skill_payload.utterance

            res = SkillResponse(outputs=[SimpleText(utterance)])

            return JsonResponse(res.to_dict(), json_dumps_params={'ensure_ascii': True})
        except:
            # TODO: Error handling
            return JsonResponse('Error occurred!')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
