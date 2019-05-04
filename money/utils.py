from prettytable import PrettyTable

class Currency:
    short_to_full = {
        'USD': 'US Dollar',
        'JPY': 'Japanese Yen',
        'BGN': 'Bulgarian Lev',
        'CZK': 'Czech Koruna',
        'DKK': 'Danish Krone',
        'GBP': 'Pound Sterling',
        'HUF': 'Hungarian Forint',
        'PLN': 'Polish Zloty',
        'RON': 'Romanian Leu',
        'SEK': 'Swedish Krona',
        'CHF': 'Swiss Franc',
        'ISK': 'Icelandic Krona',
        'NOK': 'Norwegian Krone',
        'HRK': 'Crotiana Kua',
        'RUB': 'Russian Rouble',
        'TRY': 'Turkish Lira',
        'AUD': 'Australian Dollar',
        'BRL': 'Brazilian Real',
        'CAD': 'Canadian Dollar',
        'CNY': 'Chinese Yuan Renminbi',
        'HKD': 'Hong Kong Dollar',
        'IDR': 'Indonesian Rupiah',
        'ILS': 'Israeli Shekel',
        'INR': 'Indian Rupee',
        'KRW': 'South Korean Won',
        'MXN': 'Mexican Peso',
        'MYR': 'Malaysian Ringgit',
        'NZD': 'New Zealand Dollar',
        'PHP': 'Philipine Peso',
        'SGD': 'Singapore Dollar',
        'THB': 'Thai Baht',
        'ZAR': 'South African Rand',
        'EUR': 'Euro'
    }

    @classmethod  
    def get_full_form(cls, short_form):
        short_form = short_form.upper()
        full_form = cls.short_to_full.get(short_form)
        return full_form if full_form is not None else short_form
    
    @classmethod
    def display_keys(cls):
        table = PrettyTable()
        table.title = 'Currency Key List'
        table.header = True
        table.field_names = ['Key', 'Full Form']
        for key, value in cls.short_to_full.items():
            table.add_row([key, value])
        
        print(table)