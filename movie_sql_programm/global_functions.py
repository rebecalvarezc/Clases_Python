from database_queries import *
import sqlite3
from pprint import pprint
from datetime import datetime

connection = sqlite3.connect('movie_database.db')


def create_database():
    with connection:
        connection.execute(CREATE_MOVIE_TABLE, CREATE_USER_TABLE) # Preguntar rodney


def add_movies(movie_name: str, release_date: float):
    with connection:
        connection.execute(INSERT_MOVIE, (movie_name, release_date, 0))


def show_movies():
    with connection:
        movies = connection.execute(SHOW_MOVIES).fetchall()
        for movie in movies:
            release_date = datetime.fromtimestamp(movie[2])
            pprint(f'{movie[0]}: {movie[1]} (on {release_date.strftime("%d-%m-%Y")})')


def upcoming_movies():
    with connection:
        now = datetime.now().timestamp()
        movies = connection.execute(UPCOMING_MOVIES, (now,)).fetchall()
        for movie in movies:
            release_date = datetime.fromtimestamp(movie[2])
            pprint(f'{movie[0]}: {movie[1]} (on {release_date.strftime("%d-%m-%Y")})')

# def watched_movies(username: str, movie_id: int):
#     with connection:
