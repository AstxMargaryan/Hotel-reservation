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




