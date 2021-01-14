from django.shortcuts import render
from django.http import HttpResponseRedirect
from .form import CityForm


def index(request):
    form = CityForm(request.GET);

    if not form.is_valid():
        form = CityForm()

    return render(request, 'weather/index.html', { 'form': form })