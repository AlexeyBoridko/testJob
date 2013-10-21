import json
from django.template import RequestContext
from testTicketsApp.models import UserInfo
from .models import MiddlewareRequests
from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth import logout
from forms import UserInfoForm


def main(request):
    ui = get_object_or_404(UserInfo, pk=1)
    return render(request, "testTicketsApp/main.html", {'my_info': ui})


def requests_view(request):
    requests_list = MiddlewareRequests.objects.all().order_by('id')[:10]
    return render(request, "testTicketsApp/requests.html", {'requestsList': requests_list})


def main_edit_update(request, my_info_id):
    try:
        item = get_object_or_404(UserInfo, pk=my_info_id)
    except (KeyError, UserInfo.DoesNotExist):
        return render(request, 'testTicketsApp/errors.html',
                      {'errormessage': 'Edit: UserInfo by id %s - not hound' % my_info_id})
    else:
        if request.method == 'POST' and request.is_ajax():
            form = UserInfoForm(request.POST, request.FILES, instance=item)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('update', kwargs={'my_info_id': my_info_id}))
            else:
                return render(request, "testTicketsApp/main_edit.html",
                              {"my_info": form, "userInfo": item})
        else:
            form = UserInfoForm(instance=item)
            return render(request, "testTicketsApp/main_edit.html",
                          {"my_info": form, "userInfo": item})