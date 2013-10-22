from django.contrib import admin
from .models import UserInfo, ModelChangesLog

admin.site.register(UserInfo)
admin.site.register(ModelChangesLog)
