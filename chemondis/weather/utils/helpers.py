def get_app_Id():
    app_id = '7ead097d849f6a662d7c0dcbed694654'
    return app_id

def get_weather_data(weather_data):
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
     }

    return weather