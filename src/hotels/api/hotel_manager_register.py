from django.http import HttpResponseRedirect
from ..models.hotel_manager import HotelManager
from django.shortcuts import render
from django.contrib.auth.models import User
from ..models.apikey import ApiKey


def hotel_manager_register(request):
    if request.method == "GET":
        return render(request, 'hotel_manager_register.html')
    else:
        user = User.objects.create_user(username=request.POST['username'],
                                        password=request.POST['password'])
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.save()
        manager = HotelManager(user=user)
        manager.save()
        import string
        import random
        api_key = ''.join(random.choice(string.ascii_lowercase) for _ in range(16))

        api_key_instance = ApiKey(manager=manager, api_key=api_key)
        api_key_instance.save()
        return HttpResponseRedirect('/login')