movies = [
    {'name': 'Jaws', 'director': 'Spielberg'},
    {'name': 'Silence of the Lambs', 'director': 'Pepito'},
    {'name': 'Brave', 'director': 'Maria'},
    {'name': 'Barbie', 'director': 'Stephy'}
]


def write_to_file(file_name: str, database: dict):
    key = {','.join(info) for info in [movie.keys() for movie in database]}
    values = [','.join(info) for info in [movie.values() for movie in database]]
    data = open(file_name, 'w')
    for i in key:
        data.write(i + '\n')
    for j in values:
        data.write(j + '\n')
    data.close()


write_to_file('fav_movies', movies)
