from django.urls import reverse

from .models import Log


class LogMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if not request.path.startswith(reverse('admin:index')):
            log = Log(path=request.path, method=request.method, status_code=response.status_code)
            if request.method in ['POST', 'PUT', 'PATCH']:
                log.data = request.POST.dict()
            else:
                log.data = request.GET.dict()
            log.save()
        return response
