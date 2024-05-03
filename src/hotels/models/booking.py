from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
from .hotel import Hotel
from .roomtype import RoomType


class Booking(models.Model):
    PAYMENT_STATUS = (
        ('Paid', 'Paid'),
        ('Pending', 'Pending'),
        ('Processing', 'Processing'),
        ('cancelled', 'cancelled'),
        ('failed', 'failed'),
        ('initiated', 'initiated'),
        ('unpaid', 'unpaid'),
        ('expired', 'expired')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    payment_status = models.CharField(max_length=50, choices=PAYMENT_STATUS)
    full_name = models.CharField(max_length=200)
    phone = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    hotel = models.ForeignKey(Hotel, on_delete=models.SET_NULL, null=True, blank=True)
    room_type = models.ForeignKey(RoomType, on_delete=models.SET_NULL, null=True, blank=True)
    total = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    total_days = models.PositiveIntegerField(default=0)
    num_adults = models.PositiveIntegerField(default=1)
    num_children = models.PositiveIntegerField(default=0)
    checked_in = models.BooleanField(default=False)
    checked_out = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return "{} - {} - {} - {}".format(self.user.username, self.total, self.total, self.payment_status)


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'phone', 'email', 'total', 'check_in_date', 'check_out_date', 'total_days', 'num_adults', 'num_children',
                    'hotel_name', 'room_type_name', 'payment_status']

    def get_user_info(self, obj):
        return "{} {}".format(obj.user.first_name, obj.user.last_name, obj.user.username)

    def room_type_name(self, obj):
        return "{}".format(obj.room_type.type)

    def hotel_name(self, obj):
        return "{}".format(obj.hotel.name)