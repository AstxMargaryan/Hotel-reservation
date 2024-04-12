from django.http import HttpResponseRedirect
from ..models.guest import Guest
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from ..models.apikey import ApiKey


def guest_register(request):
    if request.method == "GET":
        return render(request, 'guest_register.html')
    else:
        user = User.objects.create_user(username=request.POST['username'],
                                        password=request.POST['password'])
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.save()
        guest = Guest(user=user)
        guest.save()
        import string
        import random

        ApiKey(user=guest, api_key=''.join(random.choice(string.ascii_lowercase) for i in range(16))).save()
        return HttpResponseRedirect('/api/guest/login')


def guest_login(request):
    if request.method == "GET":
        return render(request, 'guest_login.html')
    else:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            guest = Guest.objects.get(user=user)
            api_key = ApiKey.objects.get(user=guest)
            request.session['username'] = user.username
            request.session['api_key'] = api_key.api_key
            return HttpResponseRedirect("/api/home/")
        else:
            return render(request, 'guest_login.html', context={'error_message': 'Wrong username or password'})

