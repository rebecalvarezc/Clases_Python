from http import server
import json
import requests  # Crear un requirements txt al separar este proyecto en otro repositorio
from pprint import pprint

# enter your API key in the string below:
api_key = ''
endpoint = f'http://data.fixer.io/api/latest?access_key={api_key}'

MENU = """Welcome to your currency converter.
        - Press 1 to convert.
        - Press 2 to stop the app.
        --> """


def import_jason() -> dict:
    """
    This function recovers the data from the attached json, which have information about the currencies.
    :returns: dict
    """
    with open('currency_data.json', 'r', encoding='utf-8') as data:
        currency_data = json.load(data)
    return currency_data


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
    """
    This function uses the info collected from the API & the json file to show the user the currency exchange.
    """
    try:
        amount = float(input('\nEnter the amount you want to convert: '))
        currency_data = import_jason()
        _fromCurrency = input('\nEnter your from currency: ').upper()
        _toCurrency = input('Enter your to currency: ').upper()
        rates = access_currency_info()
        conversion = round(amount * rates[_toCurrency] / rates[_fromCurrency], 2)
        print(
            f'{amount}{currency_data[_fromCurrency]["symbol"]} equals to {conversion}{currency_data[_toCurrency]["symbol"]}\n')
    except KeyError:
        print('Currency not found.\n')

    except ValueError:
        print('Introduce a valid amount.\n')


if __name__ == '__main__':
    while user_input := int(input(MENU)) != 2:
        if user_input == 1:
            currency_rate_exchange()
        else:
            print('Please select a valid option.')
    print('Goodbye :)')
