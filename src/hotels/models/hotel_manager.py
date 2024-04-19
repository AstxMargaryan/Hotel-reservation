from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User


class HotelManager(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    hotel_name = models.CharField(max_length=200)
    hotel_address = models.CharField(max_length=30)
    contact_email = models.EmailField(max_length=50)

    def str(self):
        return "{} - {} - {} - {}".format(self.user.username, self.hotel_name, self.hotel_address, self.contact_email)


@admin.register(HotelManager)
class HotelManagerAdmin(admin.ModelAdmin):
    list_display = ['get_user_info', 'hotel_name', 'hotel_address', 'contact_email']

    def get_user_info(self, obj):
        return "{} {}".format(obj.user.first_name, obj.user.last_name)