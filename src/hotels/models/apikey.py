from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User


class ApiKey(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    api_key = models.CharField(max_length=16)

    def __str__(self):
        return "{} {}".format(self.user.username, self.api_key)


@admin.register(ApiKey)
class ApiKeyAdmin(admin.ModelAdmin):
    list_display = ['id', 'get_user_info', 'api_key']


    def get_user_info(self, obj):
            return obj.user.username
