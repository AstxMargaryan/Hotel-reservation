from django.db import models
from django.contrib import admin
from .guest import Guest


class Hotel(models.Model):
    user = models.ForeignKey(Guest, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    address = models.CharField(max_length=255)
    image = models.ImageField(upload_to='')
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    views = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} ".format(self.user.user.username)


@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ['get_user_info', 'name', 'description', 'address', 'phone', 'email', 'views', 'date']

    def get_user_info(self, obj):
        return "{} {}".format(obj.user.first_name, obj.user.last_name)