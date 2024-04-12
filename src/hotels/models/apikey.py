from .guest import Guest
from django.db import models
from django.contrib import admin


class ApiKey(models.Model):
    user = models.OneToOneField(Guest, on_delete=models.CASCADE)
    api_key = models.CharField(max_length=16)

    def __str__(self):
        return "{} {}".format(self.user.user.username, self.api_key)


@admin.register(ApiKey)
class ApiKeyAdmin(admin.ModelAdmin):
    list_display =['get_user_info', 'api_key']

    def get_user_info(self, obj):
        return obj.user.user.username
    get_user_info.short_description = "User"
