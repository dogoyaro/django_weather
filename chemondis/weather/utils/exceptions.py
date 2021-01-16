class WeatherDataException(Exception):
    """ Weather Data Fetch Exception """
    def __init__(self, message):
        self.message = message

class WeatherCacheException(Exception):
    """ Weather Cache Exception """
    def __init__(self, message):
        self.message = message