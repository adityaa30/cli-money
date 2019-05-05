import requests
from prettytable import PrettyTable
from money.utils import Currency

def display_currency_rates(base_currency, time):
    """
    @param base_currency: Base currency for which the other currency rates are to
    be displayed
    """
    base_currency = base_currency.upper()
    url = 'https://api.exchangeratesapi.io/{}?base={}'.format(time, base_currency)
    try:
        r = requests.get(url=url)
        data = r.json()

        pretty_table(
            rates=data['rates'],
            base_currency=data['base'],
            date=data['date']
        )
    except KeyboardInterrupt:
        print('Cancelled the request for currency rates')
    except Exception:
        print('Some error occurred. Please check your internet connection & retry')



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