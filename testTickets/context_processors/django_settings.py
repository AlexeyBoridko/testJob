from django.conf import settings


def to_context(request):
    return {'django_settings': settings}