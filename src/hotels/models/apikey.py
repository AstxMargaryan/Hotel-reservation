from .guest import Guest
from django.db import models
from django.contrib import admin
from .hotel_manager import HotelManager


class ApiKey(models.Model):
    guest = models.OneToOneField(Guest, null=True, blank=True, on_delete=models.CASCADE)
    manager = models.OneToOneField(HotelManager, null=True, blank=True, on_delete=models.CASCADE)
    api_key = models.CharField(max_length=16)

    def str(self):
        return "{} {}".format(self.user.user.username, self.api_key)


@admin.register(ApiKey)
class ApiKeyAdmin(admin.ModelAdmin):
    list_display = ['get_user_info', 'api_key']

    def get_user_info(self, obj):
        if obj.guest:
            return obj.guest.user.username
        elif obj.manager:
            return obj.manager.user.username