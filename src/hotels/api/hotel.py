from ..models.hotel import Hotel
from django.shortcuts import render
from ..models.roomtype import RoomType
from .authentication import auth
from django.http import HttpResponse


def get_hotel_list(request):
    context = auth(request)
    if context.get('is_auth', True):
        hotels = Hotel.objects.all()
        context = {'hotels': hotels}
        return render(request, 'get_hotel_list.html', context)
    else:
        return HttpResponse("Authentication failed")


def hotel_detail(request, id):
    context = auth(request)
    if context.get('is_auth', True):
        try:
            hotel = Hotel.objects.get(id=id)
            room_types = RoomType.objects.filter(hotel=hotel)
            user_id = context.get('user_id')
            context = {
                'hotel': hotel,
                'room_types': room_types,
                'user_id': user_id
            }


            print(f"User ID: {request.user.id}")
            print(f"Is Authenticated: {request.user.is_authenticated}")

            return render(request, 'hotel_detail.html', context)
        except Hotel.DoesNotExist:
            return render(request, 'hotel_not_found.html')
    else:
        return HttpResponse("Authentication failed")