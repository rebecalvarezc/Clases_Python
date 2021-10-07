import database_queries
import sqlite3
from pprint import pprint
from datetime import datetime

connection = sqlite3.connect('movie_database.db')


def create_database():
    with connection:
        connection.execute(database_queries.CREATE_MOVIE_TABLE)


def add_movies(movie_name: str, release_date: float):
    with connection:
        movie_exists = connection.execute(database_queries.CHECK_MOVIE, (movie_name, release_date)).fetchone()
        if movie_exists is None:
            connection.execute(database_queries.INSERT_MOVIE, (movie_name, release_date, 0))
            return True
        return False


def show_movies():
    with connection:
        movies = connection.execute(database_queries.SHOW_MOVIES).fetchall()
        for movie in movies:
            release_date = datetime.fromtimestamp(movie[2])
            pprint(f'{movie[0]}: {movie[1]} (on {release_date.strftime("%b %d %Y")})')


def upcoming_movies():
    with connection:
        now = datetime.now().timestamp()
        movies = connection.execute(database_queries.UPCOMING_MOVIES, (now,)).fetchall()
        if movies is not None:
            for movie in movies:
                release_date = datetime.fromtimestamp(movie[2])
                pprint(f'{movie[0]}: {movie[1]} (on {release_date.strftime("%b %d %Y")})')
            return True
        return False


def change_movie_status(movie_id: int) -> bool:
    with connection:
        all_movies = connection.execute(database_queries.MOVIES_IDS, (movie_id,)).fetchone()
        if all_movies is not None:
            watch_date = datetime.now().timestamp()
            connection.execute(database_queries.CHANGE_WATCHED_MOVIE, (watch_date, movie_id,))
            return True
        return False


def watched_movies():
    with connection:
        movies = connection.execute(database_queries.WATCHED_MOVIES).fetchall()
        for movie in movies:
            release_date = datetime.fromtimestamp(movie[2])
            pprint(f'{movie[0]}: {movie[1]} (on {release_date.strftime("%b %d %Y")})')
