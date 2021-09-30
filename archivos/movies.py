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
    data = open(file_name, 'w')
    movie_file = csv.writer(data)
    movie_file.writerows([movie.values() for movie in movies])
    data.close()


#write_to_file('fav_movies.txt')


def human_print(file_name: str):
    data = open(file_name, 'r')
    movie_file = csv.reader(data)
    # database = [item.strip() for item in data.readlines()[1:]]
    data.close()
    print(movie_file)
    # for line in movie_file:
    #     movie_data = line.split(',')
    #     movie_name = movie_data[0].capitalize()
    #     movie_director = movie_data[1].capitalize()
    #
    #     print(f'The movie {movie_name} was directed by {movie_director}')

human_print('fav_movies.txt')
