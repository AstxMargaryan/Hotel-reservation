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
            if Guest.objects.filter(user=user).exists() or HotelManager.objects.filter(user=user).exists():
                api_key = ApiKey.objects.get(user=user)
                request.session['username'] = user.username
                request.session['api_key'] = api_key.api_key
                print("Guest authenticated", request.session.get('username'))
                return HttpResponseRedirect("/api/home")
            else:
                return render(request, 'login.html', {'error_message': 'User is not a guest or hotel manager.'})
        else:
            return render(request, 'login.html', {'error_message': 'Invalid credentials.'})
    else:
        return render(request, 'login.html')
