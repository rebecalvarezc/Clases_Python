from datetime import datetime
import global_functions
from pprint import pprint

MAIN_MENU = """\nWelcome to the watchlist app!
Please select one of the following options:
1.- Add a new movie.
2.- View upcoming movies.
3.- View all movies.
4.- Add watched movies.
5.- View watched movies.
6.- Add user to the app.
7.- Exit.

Your selection: """


def add_function():
    movie_name = input('Movie name: ').title()
    date = input('Release date (dd-mm-yyyy): ')
    release_date = datetime.strptime(date, '%d-%m-%Y').timestamp()
    added = global_functions.add_movies(movie_name, release_date)
    if added:
        print('Movie successfully added :)\n')
    else:
        print('The movie is already saved in our database.')


def print_movies(movies: list):
    for movie in movies:
        movie_id = movie[0]
        title = movie[1]
        release_date = datetime.fromtimestamp(movie[2])
        pprint(f'{movie_id}: {title} (on {release_date.strftime("%b %d %Y")})')


def show_upcoming_movies():
    any_upcoming_movie = global_functions.get_movies(True)
    if not any_upcoming_movie:
        print('There aren\'t any upcoming movies.')
    else:
        print('-- Upcoming movies --')
        print_movies(any_upcoming_movie)
        print('-----')


def add_watched_movie():
    while True:
        print_movies(global_functions.get_movies())
        try:
            movie_id = int(input('Movie ID: '))
            movie_watched = global_functions.change_movie_status(movie_id)
            if movie_watched:
                print('Movie status changed :)')
            else:
                print('Movie ID not found.')
            break
        except ValueError:
            print('Introduce a number in "Movie ID".')
            continue


def user_interface():
    while (user_selection := int(input(MAIN_MENU))) != 7:
        global_functions.create_database()
        if user_selection == 1:
            add_function()

        elif user_selection == 2:
            show_upcoming_movies()

        elif user_selection == 3:
            print('-- All movies --')
            movies = global_functions.get_movies()
            print_movies(movies)
            print('------')

        elif user_selection == 4:
            add_watched_movie()

        elif user_selection == 5:
            print('\n-- Watched movies --')
            print_movies(global_functions.watched_movies())

        elif user_selection == 6:
            pass

        else:
            print('Introduce a valid option.')
    print('Goodbye :)')


if __name__ == '__main__':
    user_interface()