import requests
import json
from config import symbols


class APIException(Exception):
    pass


class CurrencyExchange:
    @staticmethod
    def get_price(quote: str, base: str, amount: str):
        if quote == base:
             raise APIException(f'Невозможно перевести одинаковые валюты {base}')

        try:
           quote_ticker = symbols[quote]
        except KeyError:
            raise APIException(f'Не удалось обработать валюту {quote}')
        try:
            base_ticker = symbols[base]
        except KeyError:
            raise APIException(f'Не удалось обработать валюту {base}')
        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f'Не удалось обработать количество {amount}')

        r = requests.get(f'https://api.exchangeratesapi.io/latest?base={quote_ticker}&rates={base_ticker}')
        total_base = json.loads(r.content)[symbols[base]]

        return total_base
