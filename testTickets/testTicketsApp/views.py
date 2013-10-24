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
    item = get_object_or_404(UserInfo, pk=1)

    form = UserInfoForm(instance=item)
    context = dict({'user_info': item, 'form': form})
    return render(request, template, context)


def requests_view(request):
    template = "testTicketsApp/requests.html"
    requests_list = MiddlewareRequests.objects.all().order_by('id')[:10]

    form = RequestsForm(instance=requests_list[0])
    context = dict({'requests_list': requests_list, 'form': form})
    return render(request, template, context)


def main_edit_update(request, item_id):
    template = "testTicketsApp/main_edit.html"
    try:
        item = get_object_or_404(UserInfo, pk=item_id)
        context = dict({'user_info': item})
    except (KeyError, UserInfo.DoesNotExist):
        template = 'testTicketsApp/errors.html'
        context = dict({'error_message': 'Edit: UserInfo by id %s - not hound' % item_id})
    else:
        form = UserInfoForm(request.POST or None, request.FILES or None, instance=item)
        context.update({'form': form})
        request_method = request.method

        if request_method == 'POST':
            if request.is_ajax():
                if form.is_valid():
                    form.save()
                    return HttpResponseRedirect(reverse('update', kwargs={'item_id': item_id}))
            else:
                template = 'testTicketsApp/errors.html'
                context = dict({'error_message': 'Update user contact info: Post is not ajax'})

    return render(request, template, context)
