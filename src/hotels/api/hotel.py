from ..models.hotel import Hotel
from django.shortcuts import render
from .authentication import auth


def choose_hotel(request):
    is_auth, context = auth(request)
    if is_auth:
        hotels = Hotel.objects.all()
        context = {'hotels': hotels}
        return render(request, 'index.html', context)