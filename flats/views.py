from django.http import HttpResponse

from .models import Flat


def index(request):
    latest_flats_list = Flat.objects.order_by('-pub_date')[:6]
    output = ', '.join([flat.about for flat in latest_flats_list])
    return HttpResponse(output)


def detail(request, flat_id):
    return HttpResponse("You're looking at flat %s." % flat_id)
