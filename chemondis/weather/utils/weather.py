import aiohttp

from weather.models import Weather
from .cache import weather_cache


class WeatherDataException(Exception):
    """ Weather Data Fetch Exception """


class WeatherData:
    """ Weather Data Context Manager """

    def __init__(self, city, appId, lang='en', units='metric', **kwargs):
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

        self.params = {}
        self.params["city"] = city
        self.params["appId"] = appId
        self.params["lang"] = lang
        self.params["units"] = units
        self.params.update(**kwargs)


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
            units = params["units"]
            lang = params["lang"]

            try:
                async with session.get(
                    "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units={}&lang={}".format(
                        city, appId, units, lang
                    )
                ) as response:
                    weatherResponse = await response.json()
                    if weatherResponse.get("cod") != 200:
                        raise WeatherDataException(weatherResponse.get("message"))

                    weather = Weather(weatherResponse)
                    weatherData = weather.get_data()

                    return weatherData
            except Exception as exc:
                # TODO: Log exceptions in api call
                raise WeatherDataException(
                   "Error fetching weather information: {}".format(str(exc))
                )
