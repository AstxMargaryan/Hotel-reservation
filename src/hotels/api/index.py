from django.shortcuts import render
from .authentication import auth


def index2(request):
    return render(request, 'firstpage.html')


def home_page(request):
    context=auth(request)
    return render(request, 'index.html', context)



