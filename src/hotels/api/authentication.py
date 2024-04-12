from ..models.guest import Guest
from ..models.apikey import ApiKey


def auth(obj):
        username = obj.session.get('username')
        api_key = obj.session.get('api_key')
        is_auth = True
        context = {}
        try:
            guest = Guest.objects.get(user__username=username)
            apk = ApiKey.objects.get(user=guest, api_key=api_key)
        except Guest.DoesNotExist:
            is_auth = False
            context = {'error': 'User not found with given username'}
        except ApiKey.DoesNotExist:
            is_auth = False
            context = {'error': 'ApiKey does not match'}
        else:
            context = {
                'name': "{} {}".format(guest.user.first_name, guest.user.last_name),
                'username': username,
                'user_id': guest.id
            }

        return is_auth, context