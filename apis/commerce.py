from woocommerce import API
from pprint import pprint
from datetime import datetime
capi = API(
    url='',
    consumer_key='',
    consumer_secret='',
    wp_api=True,
    version='wc/v3')

date = {'after': datetime(2021,8,15)}
info = capi.get(endpoint='orders', params=date).json()


def get_info(order, *attributes):
    for item in attributes:
        if item not in order.keys():
            return None

        order = order.get(item)

    if order is None:
        return {}
    return order


pprint([get_info(order, 'billing', 'email') for order in info])
