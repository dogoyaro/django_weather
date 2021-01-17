import aiohttp
import asyncio
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.conf import settings

from .form import CityForm
from .utils.weather import WeatherData, WeatherDataException


async def index(request):
    """ Index view for providing weather form """
    try:
        form = CityForm(request.GET)
        appId = settings.APP_ID
        response = {}

        if not form.is_valid():
            form = CityForm()

        else:
            city = form.cleaned_data["city"]
            lang = request.LANGUAGE_CODE
            try:
                async with WeatherData(city, appId, lang=lang) as weather:
                    response["weather"] = weather
            except WeatherDataException as exc:
                error = {"message": str(exc)}
                response["error"] = error

    except Exception as exc:
        # TODO: Log Fatal Error for debugging
        if settings.DEBUG:
            raise
        error = {"message": "Something went wrong, Please try again"}
        response["error"] = error

    response["form"] = form
    return render(request, "weather/index.html", response)
