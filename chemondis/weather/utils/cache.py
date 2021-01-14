from django.core.cache import cache
from django.conf import settings
from .exceptions import WeatherCacheException


def weather_cache(weather_api_fetch):
    async def get_data(self, *args, **kwargs):
        params = self.params
        cache_key = params['city'] + params.get('units', 'metric') + params.get('lang', 'en')
        try:
            result = cache.get(cache_key)

        except Exception as exc:
            # TODO: log cache failure
            pass

        finally:
            if not result:
                result = await weather_api_fetch(self, *args, **kwargs)
                cache.add(cache_key, result, settings.CACHE_TIMEOUT)

        return result
    return get_data