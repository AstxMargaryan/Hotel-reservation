from .authentication import auth
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, reverse
from django.utils import timezone
from ..models.hotel_manager import HotelManager
from ..models.hotel import Hotel
from ..models.roomtype import RoomType


def add_hotel_page(request):
    context = auth(request)
    print('innn ', context)
    if not context.get('is_auth', True):
        return HttpResponse("Unauthorized")
    if context.get('is_hotel_manager', True):
        print('oonnn ', context)
        return render(request, 'add_hotel.html')


def create_hotel(request):
    context = auth(request)
    if not context.get('is_auth', True):
        return HttpResponse("Unauthorized")
    if context.get('is_hotel_manager', True):
        if request.method == "POST":
            name = request.POST.get('name')
            description = request.POST.get('description')
            address = request.POST.get('address')
            phone = request.POST.get('phone')
            email = request.POST.get('email')
            image = request.FILES.get('image')
            views = 0
            stars = request.POST.get('stars', 0)
            date = timezone.now()

            user_id = context.get('user_id')
            hotel_manager = HotelManager.objects.get(id=user_id)

            hotel = Hotel.objects.create(
                user=hotel_manager,
                name=name,
                description=description,
                address=address,
                phone=phone,
                email=email,
                image=image,
                views=views,
                stars=stars,
                date=date

                                         )

            room_type_name = request.POST.get('type')
            price_per_night = request.POST.get('price_per_night')
            number_of_beds = int(request.POST.get('number_of_beds', 0))
            room_capacity = int(request.POST.get('room_capacity', 0))
            room_count = int(request.POST.get('room_count', 0))

            room_type = RoomType.objects.create(
                hotel=hotel,
                type=room_type_name,
                price_per_night=price_per_night,
                number_of_beds=number_of_beds,
                room_capacity=room_capacity,
                is_available=True,
                room_count=room_count
            )
            return HttpResponseRedirect(reverse('hotel_detail', kwargs={'id': hotel.id}))
        else:
            return render(request, 'create_hotel.html')


def my_hotels(request):
    context = auth(request)
    if not context.get('is_auth', True):
        return HttpResponse("Unauthorized")
    if context.get('is_hotel_manager', True):
        user_id = context.get('user_id')
        hotels = Hotel.objects.filter(user_id=user_id)
        print(context)
        print("Debug: is_hotel_manager =", context['is_hotel_manager'])
        return render(request, 'my_hotels.html', {'hotels': hotels})
