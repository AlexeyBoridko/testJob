from testTicketsApp.models import UserInfo
from .models import MiddlewareRequests
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
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
        if request.method == 'POST':
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('main'))

    return render(request, template, context)
