from django.db import models
from django.contrib import admin
from .hotel import Hotel
from .roomtype import RoomType


class Room(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    room_type = models.ForeignKey(RoomType, on_delete=models.CASCADE)
    room_number = models.CharField(max_length=2000)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return "{} {} ".format(self.room_number, self.is_available)


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ['hotel_info',  'room_number', 'is_available']

    def hotel_info(self, obj):
        return "{} {}".format(obj.hotel.name, obj.hotel.address)


