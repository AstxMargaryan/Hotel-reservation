from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate
from ..models.apikey import ApiKey
from ..models.guest import Guest
from ..models.hotel_manager import HotelManager


def login(request):
    if request.method == "GET":
        return render(request, 'guest_login.html')
    else:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user:
            try:
                # Check if the user is a guest
                guest = Guest.objects.get(user=user)
                api_key = ApiKey.objects.get(user=guest)
                request.session['username'] = user.username
                request.session['api_key'] = api_key.api_key
                return HttpResponseRedirect("/api/home/")
            except Guest.DoesNotExist:
                pass

            try:
                # Check if the user is a hotel manager
                hotel_manager = HotelManager.objects.get(user=user)
                api_key = ApiKey.objects.get(user=hotel_manager)
                request.session['username'] = user.username
                request.session['api_key'] = api_key.api_key
                return HttpResponseRedirect("/api/home/")
            except HotelManager.DoesNotExist:
                pass

        # Authentication failed
        return render(request, 'guest_login.html', {'error_message': 'Wrong username or password'})





