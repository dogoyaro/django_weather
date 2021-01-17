def get_wind_direction(deg):
    return deg

class Weather:
    """ Model for weather data

    Methods
    _______

    get_data():
        Return the data from weather_api call
    """
    def __init__(self, weatherData):
        """
        Parameters
        ___________

        weatherData: dict
            The weather Data gotten from the API
        """
        self.weather_data = weatherData;

    def get_data(self):
        """ Returns weather data """

        weather_data = self.weather_data
        main = weather_data['main']
        wind = weather_data['wind']
        weath = weather_data['weather'][0]
        weather = {
            'temp': main['temp'],
            'min_temp': main['temp_min'],
            'max_temp': main['temp_max'],
            'humidity': main['humidity'],
            'windspeed': wind['speed'],
            'windspeed_direction': get_wind_direction(wind['deg']),
            'description': weath['description'],
            'city': weather_data['name']
        }

        return weather