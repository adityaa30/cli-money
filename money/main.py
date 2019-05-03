import requests

def get_currency_rates(base_currency):
    base_currency = base_currency.upper()
    url = 'https://api.exchangeratesapi.io/latest?base={}'.format(base_currency)
    r = requests.get(url=url)
    data = r.json()
    return data