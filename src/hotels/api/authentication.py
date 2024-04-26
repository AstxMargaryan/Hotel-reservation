from ..models.guest import Guest
from ..models.hotel_manager import HotelManager
from ..models.apikey import ApiKey


def auth(request):
    username = request.session.get('username')
    api_key = request.session.get('api_key')
    context = {'is_auth': False, 'is_guest': False, 'is_hotel_manager': False}

    if not username:
        context['error'] = 'Username not provided in session'
        return context

    if not api_key:
        context['error'] = 'API key not provided in session'
        return context

    try:
        guest = Guest.objects.get(user__username=username)
        apk = ApiKey.objects.get(user=guest.user, api_key=api_key)
        context['is_auth'] = True
        context['name'] = f"{guest.user.first_name} {guest.user.last_name}"
        context['username'] = username
        context['user_id'] = guest.id
        context['is_guest'] = True
    except (Guest.DoesNotExist, ApiKey.DoesNotExist) as e:
        print("Error during guest authentication:", e)

    if not context['is_auth']:
        try:
            hotel_manager = HotelManager.objects.get(user__username=username)
            apk = ApiKey.objects.get(user=hotel_manager.user, api_key=api_key)
            context['is_auth'] = True
            context['name'] = f"{hotel_manager.user.first_name} {hotel_manager.user.last_name}"
            context['username'] = username
            context['user_id'] = hotel_manager.id
            context['is_hotel_manager'] = True
        except (HotelManager.DoesNotExist, ApiKey.DoesNotExist) as e:
            print("Error during hotel manager authentication:", e)



    return context



