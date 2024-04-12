"""
URL configuration for hotels project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .api.guest import guest_register, guest_login
from .api.hotel import choose_hotel
from .api.index import index
from .api.hotel_manager import hotel_manager_register, hotel_manager_login
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index),
    path('admin/', admin.site.urls),
    path('guest/register/', guest_register),
    path('api/guest/login', guest_login),
    path('api/home/', choose_hotel),
    path('manager/register/', hotel_manager_register),
    path('manager/login/', hotel_manager_login)
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
