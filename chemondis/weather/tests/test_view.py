from django.test import TestCase, AsyncClient
from asgiref.sync import async_to_sync
from weather.utils.weather import WeatherData
from unittest.mock import patch
from .base import MockSession, test_weather


class TestView(TestCase):
    def setUp(self):
        self.client = AsyncClient()

    @patch("weather.utils.weather.aiohttp.ClientSession")
    @async_to_sync
    async def test_get_form_with_weather_data(self, mock_session):
        """Test get form with city query parameters"""
        mock_session.return_value = MockSession()

        response = await self.client.get("/en/weather/?city=toronto")

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, test_weather["name"])

    async def test_get_form(self):
        """ Test get form without query parameter """
        response = await self.client.get("/en/weather")
        self.assertEqual(response.status_code, 301) 
