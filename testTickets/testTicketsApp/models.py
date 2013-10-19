from django.db import models
from datetime import datetime, timedelta


class UserInfo(models.Model):
    name = models.CharField(max_length=50, default="")
    surname = models.CharField(max_length=50, default="")
    date_of_birth = models.DateTimeField(default=lambda: datetime.now() + timedelta(days=1))
    bio = models.TextField(default="")
    email = models.EmailField(max_length=50, blank=True)
    jid = models.CharField(max_length=50, default="")
    skype_id = models.CharField(max_length=50, default="")
    other_contacts = models.TextField(default="")
    contacts = models.CharField(max_length=100, default="")
    photo = models.ImageField("Photo", upload_to="images/", blank=True, null=True)

    def set_date(self, val):
        self.date_of_birth = val

    def get_date(self):
        if not self.date_of_birth is '':
            return "%s-%s-%s" % (self.date_of_birth.year, self.date_of_birth.month, self.date_of_birth.day)
        return "1982-01-13"

    date_birth = property(get_date, set_date)


class MiddlewareRequests(models.Model):
    host = models.CharField(max_length=100, default="")
    path = models.CharField(max_length=255, default="")
    method = models.CharField(max_length=20, default="")
    runtime = models.DateTimeField(auto_now_add=True)