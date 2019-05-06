from argparse import ArgumentParser

from money.utils import Currency
from money.main import display_currency_rates, pretty_table

# Create the ArgumentParser instance
parser = ArgumentParser(prog='run.py')

# Create a mutually exclusive group as only one argument 
# will be accepted at a time
parser.add_argument(
    '-l',
    '--list', 
    action='store_true',
    default=False,
    # type=bool,
    dest='list',
    help='List all the valid currency rates',
)

parser.add_argument(
    '-b',
    '--base',
    action='store',
    default='INR',
    # type=str,
    dest='base',
    help='Base currency relative to which the currency rates are to be displayed'
)

parser.add_argument(
    '-t',
    '--time',
    action='store',
    default='latest',
    # type=str,
    dest='time',
    help='Time of which the currency dates to be displayed (YYYY-MM-DD)',
)

args = parser.parse_args()

if args.base is not None:
    base_currency = args.base
    time = args.time

    if Currency.validate_key(base_currency):
        display_currency_rates(base_currency=base_currency, time=time)
    else:
        print('{} is not a valid choice.'.format(base_currency))
        print('Please list all the valid values by doing Money -l')

elif args.list is not None and args.list:  # is True
    Currency.display_keys()

# print(currency_rates)