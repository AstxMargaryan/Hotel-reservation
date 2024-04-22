from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate
from ..models.apikey import ApiKey
from ..models.guest import Guest
from ..models.hotel_manager import HotelManager


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')


        user = authenticate(username=username, password=password)
        print(user)
        if user:
            if Guest.objects.filter(user=user).exists():
                guest = Guest.objects.get(user=user)
                api_key = ApiKey.objects.get(user=guest)
                request.session['username'] = user.username
                request.session['api_key'] = api_key.api_key
                print(request.session.get(['username']))
                print("Guest authenticated", request.session.get(['username']))
                return HttpResponseRedirect("/api/home")
            elif HotelManager.objects.filter(user=user).exists():
                hotel_manager = HotelManager.objects.get(user=user)
                api_key = ApiKey.objects.get(user=hotel_manager)
                request.session['username'] = user.username
                request.session['api_key'] = api_key.api_key
                print("Hotel manager authenticated ", request.session.get(['username']))
                return HttpResponseRedirect("/api/home")
            else:
                return render(request, 'login.html', {'error_message': 'User is not a guest or hotel manager.'})
        else:
            return render(request, 'login.html', {'error_message': 'Invalid credentials.'})
    else:
        return render(request, 'login.html')
