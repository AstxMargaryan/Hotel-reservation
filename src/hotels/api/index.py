from django.shortcuts import render
from .authentication import auth
from django.http import HttpResponse
from django.http import JsonResponse


def index(request):
    return render(request, 'login.html')


def index2(request):
    return render(request, 'firstpage.html')



def home_page(request):
    username = request.session.get('username')
    api_key = request.session.get('api_key')
    print("Session data h:", request.session)
    print("Username from session h:", username)
    print("API key from session:", api_key)
    is_auth, context = auth(request)
    if is_auth:
        return render(request, 'index.html')
    else:
        return HttpResponse("Authentication failed")



