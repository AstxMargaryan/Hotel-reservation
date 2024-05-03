import datetime
from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from ..models.booking import Booking
from ..models.hotel import Hotel
from ..models.roomtype import RoomType
from .authentication import auth
from ..models.guest import Guest
from ..models.hotel_manager import HotelManager

def booking(request):
    context = auth(request)
    if not context.get('is_auth', True):
        return HttpResponse("Unauthorized")

    if request.method == 'GET':
        hotel_id_str = request.GET.get('hotel_id')
        room_type_id_str = request.GET.get('room_type_id')
        user_id = context.get('user_id')
        is_guest = context.get('is_guest', False)
        is_hotel_manager = context.get('is_hotel_manager', False)

        if not all([user_id, hotel_id_str, room_type_id_str]):
            return HttpResponse("Invalid parameters provided.")

        try:
            if is_guest:
                user_instance = Guest.objects.get(id=user_id)
                profile_instance = user_instance.profile
                address = profile_instance.address

                email = user_instance.email
                phone = user_instance.phone_number

            elif is_hotel_manager:
                user_instance = HotelManager.objects.get(id=user_id)
                address = user_instance.address
                print(address)
                email = user_instance.email
                print(email)
                phone = user_instance.phone_number
                print(phone)

            hotel_id = int(hotel_id_str)
            room_type_id = int(room_type_id_str)
            hotel = Hotel.objects.get(pk=hotel_id)
            room_type = RoomType.objects.get(pk=room_type_id)
            context['hotel'] = hotel
            context['room_type'] = room_type
            context['address'] = address
            context['email'] = email
            context['phone'] = phone
            print(context)
            return render(request, 'booking.html', context)
        except (ValueError, Hotel.DoesNotExist, RoomType.DoesNotExist, Guest.DoesNotExist, HotelManager.DoesNotExist):
            error_message = "Invalid parameters or user."
            return render(request, 'hotel_detail.html', {'error_message': error_message})
        except Exception as e:
            error_message = str(e)
            return render(request, 'hotel_detail.html', {'error_message': error_message})

    elif request.method == "POST":
        user_id = context.get('user_id')
        hotel_id_str = request.POST.get('hotel_id')
        room_type_id_str = request.POST.get('room_type_id')
        check_in_date_str = request.POST.get('check_in_date')
        check_out_date_str = request.POST.get('check_out_date')
        num_adults = int(request.POST.get('num_adults', 1))
        num_children = int(request.POST.get('num_children', 0))
        full_name = request.POST.get('full_name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        address = request.POST.get('address')


        try:
            check_in_date = datetime.datetime.strptime(check_in_date_str, '%Y-%m-%d')
            check_out_date = datetime.datetime.strptime(check_out_date_str, '%Y-%m-%d')
        except ValueError:
            error_message = "Invalid date format."
            return render(request, 'hotel_detail.html', {'error_message': error_message})

        if not all([user_id, hotel_id_str, room_type_id_str, check_in_date,
                    check_out_date, full_name, phone, email, address]):
            error_message = "Please fill in all required fields."
            return render(request, 'hotel_detail.html', {'error_message': error_message})

        try:
            hotel_id = int(hotel_id_str)
            room_type_id = int(room_type_id_str)
            hotel = Hotel.objects.get(pk=hotel_id)
            room_type = RoomType.objects.get(pk=room_type_id)
            user_instance = User.objects.get(pk=user_id)
            if room_type.room_count <= 0:
                error_message = "No rooms available for booking"
                return render(request, 'booking.html', {'error_message': error_message})
        except (ValueError, Hotel.DoesNotExist, RoomType.DoesNotExist):
            error_message = "Invalid hotel ID or room type ID."
            return render(request, 'hotel_detail.html', {'error_message': error_message})
        except Exception as ex:
            error_message = str(ex)
            return render(request, 'hotel_detail.html', {'error_message': error_message})

        try:
            room_price = float(room_type.price_per_night)
            total_days = (check_out_date - check_in_date).days
            total_price = room_price * total_days * (num_adults + 0.5 * num_children) * 0.90

            booking = Booking.objects.create(
                user=user_instance,
                hotel=hotel,
                room_type=room_type,
                check_in_date=check_in_date,
                check_out_date=check_out_date,
                total_days=total_days,
                num_adults=num_adults,
                num_children=num_children,
                full_name=full_name,
                phone=phone,
                email=email,
                total=total_price,
                address=address
            )

            room_type.room_count -= 1
            room_type.save()

            return HttpResponseRedirect('/api/booking/success')
        except ValueError as ve:
            error_message = str(ve)
            return render(request, 'hotel_detail.html', {'error_message': error_message})
        except Exception:
            error_message = "An unexpected error occurred during booking."
            return render(request, 'hotel_detail.html', {'error_message': error_message})

    else:
        return HttpResponseRedirect('/api/home')


def booking_success(request):
    return render(request, 'booking_success.html')
