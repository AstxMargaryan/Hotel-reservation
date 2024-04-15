from ..models.hotel import Hotel
from django.shortcuts import render
from .authentication import auth
from ..models.roomtype import RoomType
from ..models.room import Room


def get_hotel_list(request):
    is_auth, context = auth(request)
    if is_auth:
        hotels = Hotel.objects.all()
        context = {'hotels': hotels,}
        return render(request, 'get_hotel_list.html', context)


def hotel_detail(request, id):
    hotel = Hotel.objects.get(id=id)
    room_type = RoomType.objects.first()
    context = {'hotel': hotel, 'room_type': room_type}
    return render(request, 'hotel_detail.html', context)


def room_type_detail(request, hotel_id, room_type_id):
    hotel = Hotel.objects.get(id=hotel_id)
    room_type = RoomType.objects.get(hotel=hotel, id=room_type_id)
    rooms = Room.objects.filter(room_type=room_type, is_available=True)
    context = {"hotel": hotel, "room_type": room_type, "rooms": rooms}
    return render(request, 'room_type_detail.html', context)
