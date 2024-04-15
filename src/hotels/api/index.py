from django.shortcuts import render
from ..models.hotel import Hotel
from .authentication import auth


def index(request):
    return render(request, 'firstpage.html')


def choose_hotel(request):
    is_auth, context = auth(request)
    if is_auth:
        return render(request, 'index.html', context)