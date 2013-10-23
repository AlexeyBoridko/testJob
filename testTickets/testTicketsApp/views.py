import json
from django.template import RequestContext
from testTicketsApp.models import UserInfo
from .models import MiddlewareRequests
from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth import logout
from forms import UserInfoForm, RequestsForm


def main(request):
    template = "testTicketsApp/main.html"
    ui = get_object_or_404(UserInfo, pk=1)

    form = UserInfoForm(instance=ui)
    context = dict({'my_info': ui, 'form': form})
    return render(request, template, context)


def requests_view(request):
    template = "testTicketsApp/requests.html"
    requests_list = MiddlewareRequests.objects.all().order_by('id')[:10]

    form = RequestsForm(instance=requests_list[0])
    context = dict({'requestsList': requests_list, 'form': form})
    return render(request, template, context)


def main_edit_update(request, my_info_id):
    template = "testTicketsApp/main_edit.html"
    try:
        item = get_object_or_404(UserInfo, pk=my_info_id)
        context = dict({'userInfo': item})
    except (KeyError, UserInfo.DoesNotExist):
        template = 'testTicketsApp/errors.html'
        context = dict({'errormessage': 'Edit: UserInfo by id %s - not hound' % my_info_id})
    else:
        form = UserInfoForm(request.POST or None, request.FILES or None, instance=item)
        context.update({'my_info': form})
        if request.method == 'POST' and request.is_ajax():
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('update', kwargs={'my_info_id': my_info_id}))

    return render(request, template, context)
