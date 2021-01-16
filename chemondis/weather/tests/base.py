from contextlib import asynccontextmanager

test_weather = {
    "coord": {"lon": 54.3667, "lat": 24.4667},
    "weather": [
        {"id": 800, "main": "Clear", "description": "clear sky", "icon": "01d"}
    ],
    "base": "stations",
    "main": {
        "temp": 21,
        "feels_like": 19.72,
        "temp_min": 21,
        "temp_max": 21,
        "pressure": 1014,
        "humidity": 64,
    },
    "visibility": 10000,
    "wind": {"speed": 3.6, "deg": 300},
    "clouds": {"all": 0},
    "dt": 1610718163,
    "sys": {
        "type": 1,
        "id": 7533,
        "country": "AE",
        "sunrise": 1610680093,
        "sunset": 1610718912,
    },
    "timezone": 14400,
    "id": 292968,
    "name": "Abu Dhabi",
    "cod": 200,
}


class MockResponse:
    @staticmethod
    async def json():
        return test_weather


class MockSession:
    """ Mock aiohttp request session context manager"""

    def _init__(self, url):
        self._text = url
        self.status = status

    @asynccontextmanager
    async def get(self, url):
        yield MockResponse()

    async def __aexit__(self, exc_type, exc, tb):
        pass

    async def __aenter__(self):
        return self
