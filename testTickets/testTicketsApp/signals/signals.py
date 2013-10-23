from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.db.models import get_models
from testTicketsApp.models import ModelChangesLog


@receiver([post_save, post_delete])
def model_changes_log(sender, **kwargs):
    db_model_name = sender.__name__

    #we don't attach to self changes
    #make sure that ModelChangesLog created after syncdb
    if db_model_name == "ModelChangesLog" or not ModelChangesLog in get_models("testTicketsApp"):
        return

    action = 'deleted'

    # Detect action 'created/updated/deleted'
    if 'created' in kwargs:
        action = 'updated'
        if kwargs['created']:
            action = 'created'

    ModelChangesLog.objects.create(action_type=action, model_name=db_model_name)
