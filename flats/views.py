from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.http import Http404

from .models import Flat


def index(request):
    latest_flats_list = Flat.objects.order_by('-pub_date')[:6]
    context = {'latest_flats_list': latest_flats_list}
    return render(request, 'flats/index.html', context)


def detail(request, flat_id):
    flat = get_object_or_404(Flat, pk=flat_id)
    return render(request, 'flats/detail.html', {'flat': flat})
