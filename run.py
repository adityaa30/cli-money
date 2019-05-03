from money.main import get_currency_rates, pretty_table

pretty_table(get_currency_rates('usd')['rates'])