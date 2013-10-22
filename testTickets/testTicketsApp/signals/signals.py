from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from testTicketsApp.models import ModelChangesLog


@receiver([post_save, post_delete])
def model_changes_log(sender, **kwargs):
    if sender is ModelChangesLog:
        return

    action = 'deleted'

    # Check changes on created or updated
    if 'created' in kwargs:
        action = 'updated'
        if kwargs['created']:
            action = 'created'

    ModelChangesLog.objects.create(action_type=action, model_name=sender.__name__)