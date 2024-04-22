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
        api_key = ''.join(random.choice(string.ascii_lowercase) for _ in range(16))

        api_key_instance = ApiKey(user=user, api_key=api_key)
        api_key_instance.save()
        return HttpResponseRedirect('/login')



