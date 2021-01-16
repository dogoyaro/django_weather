import aiohttp
import asyncio
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.conf import settings

from .form import CityForm
from .utils.weather import WeatherData
from .utils.helpers import get_app_Id
from .utils.exceptions import WeatherDataException


async def index(request):
    try:
        form = CityForm(request.GET)
        appId = get_app_Id()
        response = {}

        if not form.is_valid():
            form = CityForm()

        else:
            city = form.cleaned_data["city"]
            lang = request.LANGUAGE_CODE
            print('the lang value: ', lang)
            weather_params = {
                'lang': lang
            }
            try:
                async with WeatherData(city, appId, weather_params) as weather:
                    response["weather"] = weather
            except WeatherDataException as exc:
                error = {"message": exc.message}
                response["error"] = error

    except Exception as exc:
        # TODO: Log Fatal Error for debugging
        if settings.DEBUG:
            raise
        error = {"message": "Something went wrong, Please try again"}
        response["error"] = error

    response["form"] = form
    print("The response: ", response)
    return render(request, "weather/index.html", response)
