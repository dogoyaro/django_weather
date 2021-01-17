from django.test import TestCase
from weather.utils.weather import WeatherData
from unittest.mock import patch
from .base import MockSession


class UtilsTest(TestCase):
    @patch("weather.utils.weather.aiohttp.ClientSession")
    async def test_get_weather_data(self, mock_session):
        """ Test get weather data context manager """
        mock_session.return_value = MockSession()
        async with WeatherData("dubai", "test_app_id") as weather:
            self.assertCountEqual(
                weather.keys(),
                [
                    "temp",
                    "min_temp",
                    "max_temp",
                    "humidity",
                    "city",
                    "description",
                    "windspeed",
                    "windspeed_direction",
                ],
            )