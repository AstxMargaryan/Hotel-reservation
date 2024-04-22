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
        id = request.GET.get('hotel_id')
        checkin = request.GET.get('checkin')
        checkout = request.GET.get('checkout')
        adults = request.GET.get('adults')
        children = request.GET.get('children')
        context = {'hotel': hotel,
                   'room_types': room_types,
                   'checkin': checkin,
                   'checkout': checkout,
                   'adults': adults,
                   'children': children}
        return render(request, 'hotel_detail.html', context)
    except Hotel.DoesNotExist:
        return render(request, 'hotel_not_found.html')