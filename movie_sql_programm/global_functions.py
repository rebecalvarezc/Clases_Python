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
        connection.execute(database_queries.CREATE_USER_TABLE)
        connection.execute(database_queries.CREATE_WATCHED_TABLE)  # esto se puede resumir?


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
    with connection:
        movies = connection.cursor()
        if not upcoming:
            return movies.execute(database_queries.SHOW_MOVIES).fetchall()

        now = datetime.now().timestamp()
        upcoming_list = movies.execute(database_queries.UPCOMING_MOVIES, (now,)).fetchall()
        if upcoming_list is not None:
            return upcoming_list
        return []


def new_watched_movie(username: str, movie_id: int) -> bool:
    """
    This function changes the timestamp of a movie that's been already watched by the user.

    :param movie_id: movie ID
    :return: bool
    """
    with connection:
        all_movies = connection.execute(database_queries.MOVIES_IDS, (movie_id,)).fetchone()
        all_usernames = connection.execute(database_queries.USERS_IDS, (username,)).fetchone()
        if all_usernames is not None:
            if all_movies is not None:
                pass
                return True
            return False


def add_user(name: str, last_name: str, username: str):
    with connection:
        connection.execute(database_queries.ADD_USER, (name, last_name, username))

# def watched_movies() -> list[tuple]:
#     """
#     This function gets all movies marked as watched in the database.
#
#     :return: list[tuple]
#     """
#     with connection:
#         return connection.execute(database_queries.WATCHED_MOVIES).fetchall()
