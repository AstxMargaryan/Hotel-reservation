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
from .api.index import index, index2, home_page
from .api.guest_register import guest_register
from .api.hotel_manager_register import hotel_manager_register
from .api.hotel import get_hotel_list, hotel_detail
from .api.check_availability import check_room_availability


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', index),
    path('choose/role/', index2),
    path('guest/register/', guest_register),
    path('manager/register/', hotel_manager_register),
    path('api/home/', home_page),
    path('api/hotels/', get_hotel_list),
    path('api/hotels/', get_hotel_list),
    path('api/detail/<id>', hotel_detail, name="hotel_detail"),
    path('check-room-availability/', check_room_availability, name='check_room_availability')



]

