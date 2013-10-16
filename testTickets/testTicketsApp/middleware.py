from .models import MiddlewareRequests


class RequestsTrackerMiddleware(object):

    def process_request(self, request):
        MiddlewareRequests.objects.create(host=request.get_host(), path=request.path, method=request.method)
        return None