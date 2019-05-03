import requests
from prettytable import PrettyTable

def get_currency_rates(base_currency):
    base_currency = base_currency.upper()
    url = 'https://api.exchangeratesapi.io/latest?base={}'.format(base_currency)
    r = requests.get(url=url)
    data = r.json()
    return data

def pretty_table(rates):
    table = PrettyTable()
    table.field_names = ['Currency', 'Value']
    for key, value in rates.items():
        table.add_row([key, value])
    print(table)