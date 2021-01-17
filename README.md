Quickstart

Introduction

A Django application that accepts a city name as user input and provides current weather information, by consuming the
openweathermap API.

Other features:
    - Support for three languages, including, English, French and German
    - Error handling
    - Configurable caching to support quicker responses
    - Async API calls using aiohttp


How to run the app:
    - Clone this repository by running
        `git clone git@github.com:dogoyaro/django_weather.git`
    - Change directory into chemondis
        `cd chemondis`
    - Ensure that you have docker installed
    - Run application
        `docker-compose up`
    - Navigate to the app when on localhost port 8000 on your browser

Other Notes:
    - To change the cache time, change the CACHE_TIME setting in `chemondis/settings.py`