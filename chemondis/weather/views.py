import aiohttp
import asyncio
from django.shortcuts import render
from django.http import HttpResponseRedirect

from .form import CityForm
from .utils.weather import WeatherData
from .utils.helpers import get_app_Id, get_weather_data
from .utils.exceptions import WeatherDataException
        
async def index(request):
    form = CityForm(request.GET);
    appId = get_app_Id()

    if not form.is_valid():
        form = CityForm()

    else:
        city = form.cleaned_data['city']
        weather_params = {
            'city': 'coronada',
            'appId': '',
        }
        response = {'form': form}
        try:
            async with WeatherData(weather_params) as weather_data:
                weather = get_weather_data(weather_data)
                response['weather'] = weather
        except WeatherDataException as exc:
            error = { 'message': exc.message }
            response['error'] = error

    return render(request, 'weather/index.html', response)