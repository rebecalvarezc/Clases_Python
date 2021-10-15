from pprint import pprint
import requests

# Use your API key or Token from themoviedb.org

api_key = ' '
api_token = ''' '''

# HTTP requests
"""
Get -> grab data. returns code (200-500). Retrieve data
Put -> update a resource. it accepts a json body. returns code as well
Post -> Create a resource. accepts a json body in the request.
Delete -> to delete a resource identifies by a [!URI].(https://en.wikipedia.org/wiki/Uniform_Resource_Identifier)
"""
# First use of the API
# What's our endpoint?
movie_id = 501
endpoint_path = f'movie/{movie_id}'
api_version = 3
api_base_url = f'https://api.themoviedb.org/{api_version}/'
endpoint = f'{api_base_url}{endpoint_path}?api_key={api_key}&page=1'
# print(endpoint)
r = requests.get(endpoint)  # json={'api_key=': api_key})7
# pprint(r.json())
# TODO: como lo corro en el terminal?

# Seacrh movies by name
endpoint_path = '/search/movie'
api_version = 3
api_base_url = f'https://api.themoviedb.org/{api_version}'
search_query = 'Rebeca'
endpoint = f'{api_base_url}{endpoint_path}?api_key={api_key}&query={search_query}'
print(endpoint)
r = requests.get(endpoint)  # json={'api_key=': api_key})7
if r.status_code in range(200, 300):
    data = r.json()
    # data['results'].keys()  # to see whats in the results section
    movie_ids = set()
    for info in data['results']:
        _id = info['id']
        movie_ids.add(_id)
        title = info['title']
        release_date = info['release_date']
        print(title, release_date)
    print(f'''\nThe list of movie IDs with the query: {search_query} is = {list(movie_ids)}.
A total of: {len(list(movie_ids))} unique results.''')
