import database_queries
import sqlite3
from datetime import datetime

connection = sqlite3.connect('movie_database.db')


def create_database():
    """
    This function creates the database if it does not exists.
    """
    with connection:
        connection.execute(database_queries.CREATE_MOVIE_TABLE)


def add_movies(movie_name: str, release_date: float) -> bool:
    """
    This function adds a movie to the database.

    :param movie_name: movie name
    :param release_date: movie release date
    :return: bool
    """
    with connection:
        movie_exists = connection.execute(database_queries.CHECK_MOVIE, (movie_name, release_date)).fetchone()
        if movie_exists is None:
            connection.execute(database_queries.INSERT_MOVIE, (movie_name, release_date))
            return True
        return False


def get_movies(upcoming: bool = False) -> list[tuple]:
    """
    This function shows movie data depending on the given value.

    :param upcoming: True for upcoming movies, False for all movies
    :return: list[tuple]
    """
    if not upcoming:
        with connection:
            return connection.execute(database_queries.SHOW_MOVIES).fetchall()
    else:
        with connection:
            now = datetime.now().timestamp()
            movies = connection.execute(database_queries.UPCOMING_MOVIES, (now,)).fetchall()
            if movies is not None:
                return movies


def change_movie_status(movie_id: int) -> bool:
    """
    This function changes the timestamp of a movie that's been already watched by the user.

    :param movie_id: movie ID
    :return: bool
    """
    with connection:
        all_movies = connection.execute(database_queries.MOVIES_IDS, (movie_id,)).fetchone()
        if all_movies is not None:
            watch_date = datetime.now().timestamp()
            connection.execute(database_queries.CHANGE_WATCHED_MOVIE, (watch_date, movie_id,))
            return True
        return False


def watched_movies() -> list[tuple]:
    """
    This function gets all movies marked as watched in the database.

    :return: list[tuple]
    """
    with connection:
        return connection.execute(database_queries.WATCHED_MOVIES).fetchall()
