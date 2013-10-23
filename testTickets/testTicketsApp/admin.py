from django.contrib import admin
from .models import UserInfo, MiddlewareRequests, ModelChangesLog

admin.site.register(UserInfo)
admin.site.register(MiddlewareRequests)
admin.site.register(ModelChangesLog)
