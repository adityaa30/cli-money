from argparse import ArgumentParser

from money.utils import Currency
from money.main import get_currency_rates, pretty_table

# Create the ArgumentParser instance
parser = ArgumentParser(prog='run.py')

parser.add_argument('-b', '--base', action='store')
parser.add_argument('-l', '--list', action='store_true')
args = parser.parse_args()

if args.base is not None:
    currency_rates = get_currency_rates(args.base)
    pretty_table(
        rates=currency_rates['rates'],
        base_currency=currency_rates['base'],
        date=currency_rates['date']
    )
elif args.list is not None and args.list:  # is True
    Currency.display_keys()

# print(currency_rates)