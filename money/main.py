import requests
from prettytable import PrettyTable
from money.utils import Currency

def get_currency_rates(base_currency):
    """
    @param base_currency: Base currency for which the other currency rates are to
    be displayed
    """
    base_currency = base_currency.upper()
    url = 'https://api.exchangeratesapi.io/latest?base={}'.format(base_currency)
    r = requests.get(url=url)
    data = r.json()
    return data


def pretty_table(rates, base_currency, date):
    """
    Diplay the rates table

    @param rates: Dictionary with key as base currency & value as its rate
    @param base_currency: Base currency for which the other currency rates are to
    be displayed
    @param date: String representing the date of which the rates are displayed
    """
    base_currency = Currency.get_full_form(base_currency)
    table = PrettyTable()
    table.title = 'Base currency: {} ({})'.format(base_currency, date)
    table.header = True
    table.field_names = ['Currency', 'Value']
    for key, value in rates.items():
        table.add_row([Currency.get_full_form(key), value])

    print(table)