from http import server
import json
import requests  # Crear un requirements txt al separar este proyecto en otro repositorio
from pprint import pprint

# enter your API key in the string below:
api_key = '93e0b79c3a299c6beb5c0784ab4719b1'
endpoint = f'http://data.fixer.io/api/latest?access_key={api_key}'

MENU = """Welcome to your currency converter.
        - Press 1 to convert.
        - Press 2 to stop the app.
        --> """


def access_currency_info() -> dict:
    """
    This function access the currency info using the endpoint of the API from fixer.io.
    :returns: dict
    """
    info = requests.get(endpoint)
    if info.status_code in range(200, 300):
        return info.json()['rates']
    return {}


def currency_rate_exchange():
    amount = float(input('Enter the amount you want to convert: '))
    _fromCurrency = input('Enter your from currency: ').upper()
    _toCurrency = input('Enter your to currency: ').upper()
    rates = access_currency_info()
    conversion = round(amount * rates[_toCurrency] / rates[_fromCurrency], 2)
    return f'{amount}{}'


if __name__ == '__main__':

    while user_input := int(input(MENU)) != 2:
        if user_input == 11:
            currency_rate_exchange()
        else:
            print('Please select a valid option.')
    print('Goodbye :)')
