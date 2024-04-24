from django.shortcuts import render, redirect
from ..models.booking import Booking
from ..models.hotel import Hotel
from django.contrib.auth.models import User
from ..models.roomtype import RoomType


def create_booking(request):
    if request.method == 'POST':
        user_id = int(request.POST.get('user_id'))
        hotel_id = int(request.POST.get('hotel_id'))
        room_type_id = int(request.POST.get('room_type_id'))
        check_in_date = request.POST.get('check_in_date')
        check_out_date = request.POST.get('check_out_date')
        num_adults = int(request.POST.get('num_adults', 1))
        num_children = int(request.POST.get('num_children', 0))
        full_name = request.POST.get('full_name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')

        if not all([user_id, hotel_id, room_type_id, check_in_date, check_out_date, full_name, phone, email]):
            error_message = "Please fill in all required fields."
            return render(request, 'error.html', {'error_message': error_message})

        try:
            user = User.objects.get(pk=user_id)
            hotel = Hotel.objects.get(pk=hotel_id)
            room_type = RoomType.objects.get(pk=room_type_id)
        except (User.DoesNotExist, Hotel.DoesNotExist, RoomType.DoesNotExist):
            error_message = "Invalid user, hotel, or room type."
            return render(request, 'error.html', {'error_message': error_message})

        total_days = (check_out_date - check_in_date).days
        room_price = float(room_type.price_per_night)
        total_price = room_price * total_days * (num_adults + 0.5 * num_children) * 0.90


        booking = Booking.objects.create(
            user=user,
            hotel=hotel,
            room_type=room_type,
            check_in_date=check_in_date,
            check_out_date=check_out_date,
            num_adults=num_adults,
            num_children=num_children,
            full_name=full_name,
            phone=phone,
            email=email,
            total=total_price,
            payment_status='Pending'
        )

        return redirect('booking_success')
    else:
        return render(request, 'create_booking.html')
