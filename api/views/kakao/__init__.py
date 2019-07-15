# Code by ByungWook.Kang @lesimor
from django.http import JsonResponse
from django.views import View


class KakaoSkill(View):
    def post(self, request, *args, **kwargs):
        try:
            # Get payload from request
            # Generate appropriate template
            return JsonResponse({}, json_dumps_params={'ensure_ascii': True})
        except:
            # TODO: Error handling
            return JsonResponse('Error occurred!')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


