from django.db import models
from django.contrib import admin
from .hotel import Hotel
from .roomtype import RoomType
from .guest import Guest
from .room import Room


class Booking(models.Model):
    PAYMENT_STATUS = (
        ('paid', 'paid'),
        ('pending', 'pending'),
        ('processing', 'processing'),
        ('cancelled', 'cancelled'),
        ('failed', 'failed'),
        ('cancelled', 'cancelled'),
        ('initiated', 'initiated'),
        ('unpaid', 'unpaid'),
    )
    user = models.ForeignKey(Guest, on_delete=models.SET_NULL, null=True, blank=True)
    hotel = models.ForeignKey(Hotel, on_delete=models.SET_NULL, null=True, blank=True)
    room_type = models.ForeignKey(RoomType, on_delete=models.SET_NULL, null=True, blank=True)
    room = models.ManyToManyField(Room)
    payment_status = models.CharField(max_length=40, choices=PAYMENT_STATUS)
    full_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=50)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    check_in_date = models.DateField()
    checkout_date = models.DateField()
    total_days = models.PositiveIntegerField(default=0)
    num_adults = models.PositiveIntegerField(default=1)
    num_children = models.PositiveIntegerField(default=1)

    checked_in = models.BooleanField(default=False)
    checked_out = models.BooleanField(default=False)

    def __str__(self):
        return "{} {} {} ".format(self.payment_status, self.full_name, self.total_price)


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['hotel_info', 'rooms_info', 'room_type_info', 'payment_status', 'full_name', 'total_price',
                    'checked_in', 'checked_out', 'num_adults', 'num_children']

    def hotel_info(self, obj):
        return "{} {}".format(obj.hotel.name, obj.hotel.address)

    def room_type_info(self, obj):
        return obj.room_type.type

    def rooms_info(self, obj):
        return obj.room.is_available
