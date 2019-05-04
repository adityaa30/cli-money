from money.main import get_currency_rates, pretty_table

currency_rates = get_currency_rates('inr')
pretty_table(
    rates=currency_rates['rates'],
    base_currency=currency_rates['base'],
    date=currency_rates['date']
)
# print(currency_rates)