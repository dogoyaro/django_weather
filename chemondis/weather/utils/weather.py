import aiohttp

from weather.models import Weather
from .exceptions import WeatherDataException
from .cache import weather_cache


class WeatherData:
    def __init__(self, city, appId, weather_params):
        self.params = weather_params
        self.params["city"] = city
        self.params["appId"] = appId

    async def __aenter__(self):
        weather_data = await self.get_weather_data()
        self.weather_data = weather_data
        return weather_data

    @weather_cache
    async def get_weather_data(self):
        async with aiohttp.ClientSession() as session:
            params = self.params
            city = params["city"]
            appId = params["appId"]
            units = params.get("units", "metric")
            lang = params.get("lang", "en")

            try:
                async with session.get(
                    "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units={}&lang={}".format(
                        city, appId, units, lang
                    )
                ) as response:
                    weatherResponse = await response.json()
                    if weatherResponse.get("cod") != 200:
                        raise WeatherDataException(
                            message=weatherResponse.get("message")
                        )

                    weather = Weather(weatherResponse)
                    weatherData = weather.get_data()

                    return weatherData
            except Exception as exc:
                # TODO: Log exceptions in api call
                raise WeatherDataException(
                    message="Error fetching weather information: {}".format(exc.message)
                )

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        pass
