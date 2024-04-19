from django.shortcuts import render
from ..models.roomtype import RoomType


def check_room_availability(request):
    if request.method == "POST":
        check_in = request.POST.get("check_in")
        check_out = request.POST.get("check_out")
        adults = int(request.POST.get("adults", 0))
        children = int(request.POST.get("children ", 0))

    available_hotels =RoomType.objects.filter(
        is_available=True,
        room_capacity__gte=adults+children
    )

    available_hotels = {room_type.hotel for room_type in available_hotels}

    context = {
        'check_in': check_in,
        'check_out': check_out,
        'adults': adults,
        'children': children,
        'available_hotels': available_hotels
    }
    return render(request, 'available_hotels.html', context)