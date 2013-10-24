from django.core.management.base import BaseCommand
from django.db.models import get_models


class Command(BaseCommand):
    def handle(self, *args, **options):
        for model in get_models():
            result = '[%s] - model has %d object(s).\n' % (model.__name__, model.objects.count())
            self.stdout.write(result)
            self.stderr.write('error: %s' % result)
