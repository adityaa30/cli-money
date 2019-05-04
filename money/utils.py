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
    }

    @classmethod  
    def get_full_form(cls, short_form):
        full_form = cls.short_to_full.get(short_form)
        return full_form if full_form is not None else short_form
    