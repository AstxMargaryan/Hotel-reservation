from django.shortcuts import render
from ..models.hotel import Hotel
from ..models.room import Room
from ..models.roomtype import RoomType


def check_room_availability(request):
    if request.method == "POST":
        id = request.POST.get("hotel-id")
        check_in = request.POST.get("check in")
        check_out = request.POST.get("check out")
        adult = request.POST.get("adult")
        child = request.POST.get("child ")
