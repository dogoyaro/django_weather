from django.test import TestCase
from weather.utils.weather import WeatherData
from unittest.mock import patch
from .base import MockSession, test_weather


class TestView(TestCase):
    @patch("weather.utils.weather.aiohttp.ClientSession")
    def test_get_form_with_weather_data(self, mock_session):
        mock_session.return_value = MockSession()

        response = self.client.get("/weather/?city=toronto")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, test_weather["name"])

    def test_get_form(self):
        response = self.client.get("/weather")
        self.assertEqual(response.status_code, 301) 