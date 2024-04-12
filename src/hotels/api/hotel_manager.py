from django.http import HttpResponseRedirect
from ..models.guest import Guest
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from ..models.apikey import ApiKey


def hotel_manager_register(request):
    if request.method == "GET":
        return render(request, 'hotel_manager_register.html')
    else:

        user = User.objects.create_user(username=request.POST['username'],
                                        password=request.POST['password'])
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.hotel_name = request.POST['hotel_name']
        user.save()
        import string
        import random

        ApiKey(user=user, api_key=''.join(random.choice(string.ascii_lowercase) for i in range(16))).save()
        return HttpResponseRedirect('/manager/login/')


def hotel_manager_login(request):
    if request.method == "GET":
        return render(request, 'hotel_manager_login.html')
    else:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            user = User.objects.get(user=user)
            api_key = ApiKey.objects.get(user=user)
            request.session['username'] = user.username
            request.session['api_key'] = api_key.api_key
            return HttpResponseRedirect("/api/home/")
        else:
            return render(request, 'hotel_manager_login.html', context={'error_message': 'Wrong username or password'})

