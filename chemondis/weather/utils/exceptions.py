class WeatherDataException(Exception):
    def __init__(self, message):
        self.message = message

class WeatherCacheException(Exception):
    def __init__(self, message):
        self.message = message