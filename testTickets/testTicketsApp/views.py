from testTicketsApp.models import UserInfo
from .models import MiddlewareRequests
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import logout
from django.core.exceptions import ValidationError, NON_FIELD_ERRORS


def main(request):
    ui = get_object_or_404(UserInfo, pk=1)
    return render(request, "testTicketsApp/main.html", {'my_info': ui})


def requests_view(request):
    requests_list = MiddlewareRequests.objects.all().order_by('id')[:10]
    return render(request, "testTicketsApp/requests.html", {'requestsList': requests_list})


def main_edit_update(request, my_info_id):
    try:
        my_info = get_object_or_404(UserInfo, pk=my_info_id)
    except (KeyError, UserInfo.DoesNotExist):
        return render(request, 'testTicketsApp/errors.html',
                      {'errormessage': 'Edit: UserInfo by id %s - not hound' % my_info_id})
    else:
        if request.method == 'GET':
            return render(request, "testTicketsApp/main_edit.html", {'my_info': my_info})

        if request.method == 'POST':
            my_info.name = request.POST['name']
            my_info.surname = request.POST['surname']
            my_info.date_birth = request.POST['date_of_birth']
            my_info.contacts = request.POST['contacts']
            my_info.email = request.POST['email']
            my_info.jid = request.POST['jid']
            my_info.skype_id = request.POST['skype_id']
            my_info.other_contacts = request.POST['other_contacts']
            my_info.bio = request.POST['bio']

            if 'photo_file' in request.FILES:
                my_info.photo = request.FILES['photo_file']

            try:
                my_info.full_clean()
            except ValidationError, e:
                return render(request, "testTicketsApp/main_edit.html", {'my_info': my_info, 'validationError': e})
            else:
                my_info.save()
                return HttpResponseRedirect(reverse('main'))