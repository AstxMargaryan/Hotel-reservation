from django.shortcuts import render
from .authentication import auth
from django.http import HttpResponse
from django.http import JsonResponse


def index2(request):
    return render(request, 'firstpage.html')


def home_page(request):
    context = auth(request)
    if context.get('is_auth', True):
        return render(request, 'index.html')
    else:
        return HttpResponse("Authentication failed")



