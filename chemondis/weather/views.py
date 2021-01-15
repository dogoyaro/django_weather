import aiohttp
import asyncio
from django.shortcuts import render
from django.http import HttpResponseRedirect

from .form import CityForm
from .utils.weather import WeatherData
from .utils.helpers import get_app_Id, get_weather_data
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
            weather_params = {}
            try:
                async with WeatherData(city, appId, weather_params) as weather_data:
                    weather = get_weather_data(weather_data)
                    response["weather"] = weather
            except WeatherDataException as exc:
                error = {"message": exc.message}
                response["error"] = error

    except Exception:
        # TODO: Log Fatal Error for debugging
        error = {"message": "Something went wrong, Please try again"}
        response["error"] = error

    response["form"] = form
    print("The response: ", response)
    return render(request, "weather/index.html", response)
