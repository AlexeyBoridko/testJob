from testTicketsApp.models import UserInfo
from .models import MiddlewareRequests
from django.shortcuts import render, get_object_or_404


def main(request):
    ui = get_object_or_404(UserInfo, pk=1)
    return render(request, "testTicketsApp/main.html", {'myinfo': ui})


def requests_view(request):
    requests_list = MiddlewareRequests.objects.all().order_by('id')[:10]
    return render(request, "testTicketsApp/requests.html", {'requestsList': requests_list})