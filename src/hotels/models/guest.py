import datetime
from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User


class Guest(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=30)
    date_of_birth = models.DateField(default=datetime.date.today)

    def __str__(self):
        return "{} - {} - {} - {}".format(self.user.username, self.address, self.phone_number, self.date_of_birth)


@admin.register(Guest)
class GuestAdmin(admin.ModelAdmin):
    list_display = ['id', 'get_user_info', 'address', 'phone_number', 'date_of_birth']

    def get_user_info(self, obj):
        return "{} {}".format(obj.user.first_name, obj.user.last_name, obj.user.username)
