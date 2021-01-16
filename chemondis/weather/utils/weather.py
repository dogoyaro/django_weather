import aiohttp

from weather.models import Weather
from .exceptions import WeatherDataException
from .cache import weather_cache


class WeatherData:
    """ Weather Data Context Manager """
    def __init__(self, city, appId, weather_params):
        """
        Parameters
        __________
        city:
            The city for which weather data is requested
        appId:
            The application id for the weather api
        weather_params:
            The optional weather params
        """

        self.params = weather_params
        self.params["city"] = city
        self.params["appId"] = appId


    async def __aenter__(self):
        weather_data = await self.__get_weather_data()
        self.weather_data = weather_data
        return weather_data

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        pass

    @weather_cache
    async def __get_weather_data(self):
        """
        Make weather data API request
        """
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