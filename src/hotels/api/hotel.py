from ..models.hotel import Hotel
from django.shortcuts import render


def choose_hotel(request):
    hotels = Hotel.objects.all()
    context = {'hotels': hotels}
    return render(request, 'index.html', context)