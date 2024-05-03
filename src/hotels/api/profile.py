import datetime
from .authentication import auth
from django.shortcuts import render
from django.http import HttpResponse
from ..models.guest import Guest
from ..models.booking import Booking
from ..models.hotel_manager import HotelManager


def profile(request):
    context = auth(request)
    if not context.get('is_auth', True):
        return HttpResponse("Unauthorized")

    user_id = context.get('user_id')
    is_guest = context.get('is_guest', False)
    is_hotel_manager = context.get('is_hotel_manager', False)

    if is_guest:
        user_instance = Guest.objects.get(id=user_id)

    elif is_hotel_manager:
        user_instance = HotelManager.objects.get(id=user_id)

    else:
        return HttpResponse("Invalid user type")

    if request.method == "POST":
        address = request.POST.get('address')
        phone_number = request.POST.get('phone_number')
        date_of_birth = request.POST.get('date_of_birth')
        email = request.POST.get('email')

        if is_guest:
            if address:
                user_instance.address = address
            if phone_number:
                user_instance.phone_number = phone_number
            if date_of_birth:
                user_instance.date_of_birth = date_of_birth
            if email:
                user_instance.email = email
            user_instance.save()
        elif is_hotel_manager:
            if address:
                user_instance.address = address
            if phone_number:
                user_instance.phone_number = phone_number
            if date_of_birth:
                user_instance.date_of_birth = date_of_birth
            if email:
                user_instance.email = email
            user_instance.save()

    context['profile'] = {
        'address': user_instance.address,
        'phone_number': user_instance.phone_number,
        'date_of_birth': user_instance.date_of_birth,
        'email': user_instance.email,
    }

    return render(request, 'profile.html', context)


def user_bookings(request):
    context = auth(request)
    if not context.get('is_auth',True):
        return HttpResponse("Unauthorized")
    user_id = context.get('user_id')
    bookings = Booking.objects.filter(user_id=user_id)
    if context.get('is_guest', True):
        guest = Guest.objects.get(id=user_id)
        return render(request, 'user_bookings.html', {'guest': guest, 'bookings': bookings})
    elif context.get('is_hotel_manager', True):
        hotel_manager = HotelManager.objects.get(id=user_id)
        return render(request, 'user_bookings.html', {'hotel_manager': hotel_manager, 'bookings': bookings})



