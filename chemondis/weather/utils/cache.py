from django.core.cache import cache
from django.conf import settings


def weather_cache(weather_api_fetch):
    """ Weather cache decorator """
    async def get_data(self, *args, **kwargs):
        """ Wrapper function to get data from cache
        
            Creates a cache key using provided params and
            returns the result of getting the weather data from the cache
            or runs the decorated function to get the weather data
         """

        params = self.params

        cache_key = params['city'] + params.get('units', 'metric') + params.get('lang', 'en')
        cache_key = cache_key.replace(' ', '_')

        result = None
        try:
            result = await cache.get(cache_key)

        except Exception as exc:
            # TODO: log cache failure
            pass

        finally:
            if not result:
                result = await weather_api_fetch(self, *args, **kwargs)
                cache.add(cache_key, result, settings.CACHE_TIMEOUT)

        return result
    return get_data
