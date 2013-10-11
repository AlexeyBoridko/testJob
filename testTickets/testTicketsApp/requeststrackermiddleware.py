from .models import MiddlewareRequests


class RequestsTrackerMiddleware:
    def __init__(self):
        pass

    def process_request(self, request):
        MiddlewareRequests.objects.create(host=request.get_host(), path=request.path, method=request.method)
        return None