import csv

movies = [
    {'name': 'Jaws', 'director': 'Spielberg'},
    {'name': 'Silence of the Lambs', 'director': 'Pepito'},
    {'name': 'Brave', 'director': 'Maria'},
    {'name': 'Barbie', 'director': 'Stephy'}
]


# def write_to_file(file_name: str):
#     data = open(file_name, 'w')
#     data.write('name,director \n')
#     for movie in movies:
#         data.write(f"{movie.get('name')},{movie.get('director')}\n")
#     data.close()


def write_to_file(file_name: str):
    data = open(file_name, 'w', newline='')
    movie_file = csv.DictWriter(data, ['name', 'director'])
    movie_file.writeheader()
    movie_file.writerows(movies)
    data.close()


# write_to_file('fav_movies.csv')


def human_print(file_name: str):
    data = open(file_name, 'r')
    movie_file = csv.DictReader(data)
    for line in movie_file:
        movie_name = line['name']
        movie_director = line['director']
        print(f'The movie {movie_name} was directed by {movie_director}')
    data.close()


human_print('fav_movies.csv')
