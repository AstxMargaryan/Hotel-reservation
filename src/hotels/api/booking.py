from django.shortcuts import render, HttpResponse
from django.contrib.auth.models import User
from ..models.booking import Booking
from ..models.hotel import Hotel
from ..models.roomtype import RoomType
from django.utils.dateparse import parse_date
from .authentication import auth


def booking(request):
    if request.method == 'POST':
        context = auth(request)
        if context.get('is_auth', True):
            user_id = context.get('user_id')
            hotel_id_str = request.POST.get('hotel_id')
            room_type_id_str = request.POST.get('room_type_id')
            check_in_date = request.POST.get('check_in_date')
            check_out_date = request.POST.get('check_out_date')
            num_adults = int(request.POST.get('num_adults', 1))
            num_children = int(request.POST.get('num_children', 0))
            full_name = request.POST.get('full_name')
            phone = request.POST.get('phone')
            email = request.POST.get('email')
            check_in_date = parse_date(check_in_date)
            check_out_date = parse_date(check_out_date)

            total_days = (check_out_date - check_in_date).days

            if not all([user_id, hotel_id_str, room_type_id_str, check_in_date,
                        check_out_date, full_name, phone, email]):
                error_message = "Please fill in all required fields."
                return render(request, 'hotel_detail.html', {'error_message': error_message})

            try:
                hotel_id = int(hotel_id_str)
                room_type_id = int(room_type_id_str)
                hotel = Hotel.objects.get(pk=hotel_id)
                room_type = RoomType.objects.get(pk=room_type_id)
                user_instance = User.objects.get(pk=user_id)
            except ValueError:
                return render(request, 'error.html', {'error_message': "Invalid hotel ID or room type ID."})
            except Hotel.DoesNotExist:
                return render(request, 'error.html', {'error_message': "Invalid hotel."})
            except RoomType.DoesNotExist:
                return render(request, 'error.html', {'error_message': "Invalid room type."})
            except Exception:
                return render(request, 'error.html', {'error_message': "An error occurred during booking."})

            try:
                room_price = float(room_type.price_per_night)
                total_price = room_price * total_days * (num_adults + 0.5 * num_children) * 0.90

                booking = Booking.objects.create(
                    user=user_instance,
                    hotel=hotel,
                    room_type=room_type,
                    check_in_date=check_in_date,
                    check_out_date=check_out_date,
                    num_adults=num_adults,
                    num_children=num_children,
                    full_name=full_name,
                    phone=phone,
                    email=email,
                    total=total_price,
                )

                return render(request, 'booking_success.html')
            except ValueError as ve:
                return render(request, 'error.html', {'error_message': str(ve)})
            except Exception:
                return render(request, 'error.html', {'error_message': "An unexpected error occurred during booking."})
        else:
            return HttpResponse("Unauthorized")
    else:
        return HttpResponse("Method not allowed")
