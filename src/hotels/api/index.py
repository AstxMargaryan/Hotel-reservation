from django.shortcuts import render
from .authentication import auth


def index(request):
    is_auth, context = auth(request)
    if is_auth:
        return render(request, 'firstpage.html')