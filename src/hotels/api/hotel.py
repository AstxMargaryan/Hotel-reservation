from ..models.hotel import Hotel
from django.shortcuts import render
from ..models.roomtype import RoomType
from .authentication import auth
from django.http import HttpResponse


def get_hotel_list(request):
    context = auth(request)
    hotels = Hotel.objects.all()
    context['hotels'] = hotels
    return render(request, 'get_hotel_list.html', context)


def hotel_detail(request, id):
    context = auth(request)
    hotel = Hotel.objects.get(id=id)
    room_types = RoomType.objects.filter(hotel=hotel)
    print(room_types)
    context['hotel'] = hotel
    context['room_types'] = room_types
    print("Context after hotels retrieval:", context)
    return render(request, 'hotel_detail.html', context)

