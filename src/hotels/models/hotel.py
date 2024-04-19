from django.db import models
from django.contrib import admin
from .hotel_manager import HotelManager


class Hotel(models.Model):
    user = models.ForeignKey(HotelManager, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    address = models.CharField(max_length=255)
    image = models.ImageField(upload_to='profile_pic', default='default.jpg')
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    views = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True)
    stars = models.IntegerField(default=0)

    def str(self):
        return "{} ".format(self.name)


@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ['get_user_info',  'name', 'description', 'address', 'phone', 'email', 'views', 'date']

    def get_user_info(self, obj):
        return "{} {}".format(obj.user.user.first_name, obj.user.user.last_name)