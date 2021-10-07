from datetime import datetime
from global_functions import *
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


def user_interface():
    while (user_selection := int(input(MAIN_MENU))) != 7:
        create_database()
        if user_selection == 1:
            movie_name = input('Movie name: ').title()
            date = input('Release date (dd-mm-yyyy): ')
            release_date = datetime.strptime(date, '%d-%m-%Y').timestamp()
            add_movies(movie_name, release_date)
            print('Movie successfully added :)\n')

        elif user_selection == 2:
            print('-- Upcoming movies --')
            upcoming_movies()

        elif user_selection == 3:
            print('-- All movies --')
            movies = show_movies()

        elif user_selection == 4:
            while True:
                try:
                    username = input('Username: ')
                    movie_id = int(input('Movie ID: '))
                    watched_movies(username, movie_id)
                except ValueError:
                    print('Por favor introduzca un numero en "Movie ID".')

        elif user_selection == 5:
            username = input('Username: ')
            print('\n-- Watched movies --')
            # funcion5

        elif user_selection == 6:
            username = input('Username: ')

        else:
            print('Introduce a valid option.')
    print('Goodbye :)')


if __name__ == '__main__':
    user_interface()
