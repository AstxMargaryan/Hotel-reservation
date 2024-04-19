from ..models.hotel import Hotel
from django.shortcuts import render
from ..models.roomtype import RoomType


def get_hotel_list(request):
        hotels = Hotel.objects.all()
        context = {'hotels': hotels}
        return render(request, 'get_hotel_list.html', context)


def hotel_detail(request, id):
    try:
        hotel = Hotel.objects.get(id=id)
        room_types = RoomType.objects.filter(hotel=hotel)
        context = {'hotel': hotel, 'room_types': room_types}
        return render(request, 'hotel_detail.html', context)
    except Hotel.DoesNotExist:
        return render(request, 'hotel_not_found.html')


