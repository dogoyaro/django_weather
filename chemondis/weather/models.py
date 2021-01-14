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