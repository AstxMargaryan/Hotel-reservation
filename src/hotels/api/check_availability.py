from django.urls import reverse
from django.http import HttpResponseRedirect


def check_hotel_availability(request):
    if request.method == "POST":
        check_in = request.POST.get("check_in")
        check_out = request.POST.get("check_out")
        adults = int(request.POST.get("adults", 0))
        children = int(request.POST.get("children", 0))

        url = reverse('hotel_list')
        url_with_parameters = "{}?check_in={}&check_out={}&adults={}&children={}".format(url, check_in, check_out, adults, children)
        return HttpResponseRedirect(url_with_parameters)


def add_to_selection(request):
    room_selection = {
        'id': request.GET.get('id', ''),
        'name': request.GET.get('name', ''),
        'room_type': request.GET.get('room_type', ''),
        'price': request.GET.get('price', ''),
        'num_of_beds': request.GET.get('num_of_beds', ''),
        'checkout': request.GET.get('checkout', ''),
        'checkin': request.GET.get('checkin', ''),
        'adults': request.GET.get('adults', ''),
        'children': request.GET.get('children', '')
    }

    if 'selection' in request.session:
        selection_data = request.session['selection']
        if room_selection['id'] in selection_data:
            selection_data[room_selection['id']]['adults'] = int(room_selection['adults'])
            selection_data[room_selection['id']]['children'] = int(room_selection['children'])
            request.session['selection'] = selection_data
        else:
            selection_data[room_selection['id']] = room_selection
        request.session['selection'] = selection_data

    else:
        selection_data = {room_selection['id']: room_selection}
        request.session['selection'] = selection_data

    data = {
        'data': request.session['selection'],
        'total_selected_items': request.session['selection']
    }
    return data

