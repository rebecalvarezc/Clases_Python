import sqlite3
from libros.project_sql.database_queries import *

STATUS = {True: 'Leído', False: 'No leído'}

database_name = 'rebeca_library.db'


def connect():
    return sqlite3.connect(database_name)


def create_library(connection):
    with connection:
        connection.execute(CREATE_TABLE)


def add_book(connection, name: str, author: str, status: bool = STATUS[False]):
    with connection:
        connection.execute(INSERT_BOOK, (name, author, status))


def show_books(connection):
    with connection:
        return connection.execute(SHOW_ALL_BOOKS).fetchall()
