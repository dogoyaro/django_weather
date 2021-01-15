from django.db import models

class Weather:
    def __init__(self, weatherData):
        self.weather_data = weatherData;

    def get_data(self):
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
            'windspeed_direction': wind['deg'],
            'description': weath['description'],
            'city': weather_data['name']
        }

        return weather