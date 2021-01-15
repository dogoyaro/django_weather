from django.db import models

class Weather(models.Model):
    temp = models.FloatField()
    max_temp = models.FloatField()
    min_temp = models.FloatField()
    humidity = models.FloatField()
    windspeed = models.FloatField()
    windspeed_direction = models.FloatField()
    city = models.CharField(max_length=200)
    units = models.CharField(max_length=100)
    lang = models.CharField(max_length=200)
 
    def __init__(self, weatherData):
        self.weather_data = weatherData;

    def get_weather(self):
        return {
            'temp': self.temp,
            'max_temp': self.max_temp,
            'min_temp': self.min_temp,
            'humidity': self.humidity,
            'windspeed': self.windspeed,
            'city': self.city,
            'units': self.units,
            'lang': self.lang,
        }

    def get_data(self):
        weather_data = self.weather_data
        print('The main weather data', weather_data)
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