import requests
import functools
from cachetools import cached, TTLCache

class OpenExchangeRates:
    
    APP_ID = '78b3315576864923b18a02a41b15c811'
    ENDPOINT = 'https://openexchangerates.org/api/latest.json'

    @property
    # @functools.lru_cache(maxsize=2)
    @cached(cache=TTLCache(maxsize=2, ttl=900))
    def latest_rates(self):
        return requests.get(f'{self.ENDPOINT}?app_id={self.APP_ID}').json()['rates']

    def convert_to_currency(self, from_currency, to_currency, from_amount):
        rates = self.latest_rates

        to_rate = rates[to_currency]

        if from_currency == 'USD':
            return from_amount * to_rate
        else:
            from_amount_in_usd = from_amount / rates[from_currency]
            return from_amount_in_usd * to_rate