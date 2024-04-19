from django.shortcuts import render
from .authentication import auth
from django.http import HttpResponse

def index(request):
    return render(request, 'login.html')


def index2(request):
    return render(request, 'firstpage.html')


def home_page(request):
    is_auth, context = auth(request)
    if is_auth:
        return render(request, 'index.html')
    else:
        return HttpResponse("Authentication failed")



