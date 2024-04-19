from ..models.guest import Guest
from ..models.apikey import ApiKey
from django.contrib.auth.models import User

from ..models.guest import Guest
from ..models.apikey import ApiKey

def auth(obj):
    username = obj.session.get('username')
    api_key = obj.session.get('api_key')
    is_auth = False
    context = {}

    if username is None or api_key is None:
        context = {'error': 'Username or API Key not found in session'}
    else:
        try:
            guest = Guest.objects.get(user__username=username)
            apk = ApiKey.objects.get(user=guest, api_key=api_key)
            context = {
                'name': "{} {}".format(guest.user.first_name, guest.user.last_name),
                'username': username,
                'user_id': guest.id
            }
            is_auth = True
        except Guest.DoesNotExist:
            context = {'error': 'User not found with given username'}
        except ApiKey.DoesNotExist:
            context = {'error': 'ApiKey does not match'}

    return is_auth, context
