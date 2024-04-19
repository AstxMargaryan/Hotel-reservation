from django.db import models
from django.contrib import admin
from .hotel import Hotel


class RoomType(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='room_types')
    type = models.CharField(max_length=20)
    price_per_night = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    number_of_beds = models.PositiveIntegerField(default=0)
    room_capacity = models.PositiveIntegerField(default=0)
    is_available = models.BooleanField(default=True)

    def str(self):
        return "{} {} {} {}".format(self.type, self.price_per_night, self.number_of_beds, self.room_capacity)


@admin.register(RoomType)
class RoomTypeAdmin(admin.ModelAdmin):
    list_display = ['hotel_info', 'type', 'price_per_night', 'number_of_beds', 'room_capacity', 'is_available']

    def hotel_info(self, obj):
        return "{} {}".format(obj.hotel.name, obj.hotel.address)