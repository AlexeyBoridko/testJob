from django.db import models
from datetime import datetime, timedelta


class UserInfo(models.Model):
    name = models.CharField(max_length=50, default="")
    surname = models.CharField(max_length=50, default="")
    date_of_birth = models.DateTimeField(default=lambda: datetime.now() + timedelta(days=1))
    bio = models.TextField(default="")
    email = models.CharField(max_length=50, default="")
    jid = models.CharField(max_length=50, default="")
    skype_id = models.CharField(max_length=50, default="")
    other_contacts = models.TextField(default="")
    contacts = models.CharField(max_length=100, default="")


    def __str__(self):
        return self.name


class MiddlewareRequests(models.Model):
    host = models.CharField(max_length=100, default="")
    path =  models.CharField(max_length=255, default="")
    method = models.CharField(max_length=20, default="")
    runtime = models.DateTimeField(auto_now_add=True)