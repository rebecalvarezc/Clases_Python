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


# write_to_file('fav_movies.txt', movies)

def human_print(file_name: str):
    data = open(file_name, 'r')
    database = [item.strip() for item in data.readlines()[1:]]
    data.close()

    for line in database:
        movie_data = line.split(',')
        movie_name = movie_data[0].capitalize()
        movie_director = movie_data[1].capitalize()

        print(f'The movie {movie_name} was directed by {movie_director}')



human_print('fav_movies')

