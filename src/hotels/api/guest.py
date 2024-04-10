from django.http import HttpResponseRedirect
from ..models.guest import Guest

from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


def register(request):
    if request.method == "GET":
        return render(request, 'register.html')
    else:
        user = User.objects.create_user(username=request.POST['username'],
                                        password=request.POST['password'])
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.save()
        guest = Guest(user=user)
        guest.save()
        return HttpResponseRedirect('/api/login')


def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            return HttpResponseRedirect("/api/home/")
        else:
            return render(request, 'login.html', context={'error_message': 'Wrong username or password'})

