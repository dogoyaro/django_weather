# Weather

## Introduction

A Django application that accepts a city name as user input and provides current weather information by consuming the
openweathermap API.



### Features:   


      - Async API calls using aiohttp
      - Configurable caching to support quicker responses
      - Error handling
      - Support for three languages, including, English, French and German
      - Clean layout of Weather information using django templates/forms.


### How to run the app:
    Pre-requisites: Docker
    
    - Ensure that you have docker installed
    - Make a copy of the .env_sample file to a .env file and replace dummy environment variables with the real values
        NB: Application Id is provided by creating an account with openweatherapi.org
    - Run application
    - Navigate to the app on localhost port 8000 on your browser



```sh
$ git clone git@github.com:dogoyaro/django_weather.git
$ cd chemondis
$ docker-compose up
```
        


Other Notes:
    - To change the cache time, change the CACHE_TIME setting in `chemondis/settings.py`
