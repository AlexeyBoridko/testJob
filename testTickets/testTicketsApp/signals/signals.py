from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from testTicketsApp import models


@receiver([post_save, post_delete])
def model_changes_log(sender, **kwargs):

    db_model_name = sender.__name__

    if db_model_name == "ModelChangesLog":
        return

    # make sure that ModelChangesLog created after syncdb
    try:
        action = 'deleted'

        # Check changes on created or updated. I know it is not good idea :(
        if 'created' in kwargs:
            action = 'updated'
            if kwargs['created']:
                action = 'created'

        models.ModelChangesLog.objects.create(action_type=action, model_name=db_model_name)
    except:
        return
