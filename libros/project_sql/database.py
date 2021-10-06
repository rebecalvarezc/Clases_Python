import sqlite3

from libros.project_sql.database_queries import *

STATUS = {True: 'Leído', False: 'No leído'}

connection = sqlite3.connect('rebeca_library.db')


def create_library():
    with connection:
        connection.execute(CREATE_TABLE)


def add_book(title: str, author: str, status: bool = STATUS[False]):
    with connection:
        book_list = connection.execute(EXISTING_BOOKS).fetchall()
        if (title, author) not in book_list:
            connection.execute(INSERT_BOOK, (title, author, status))
            return True
        else:
            return False


def show_books() -> list[tuple]:
    with connection:
        return connection.execute(SHOW_ALL_BOOKS).fetchall()


def change_book_status(book_id: int):
    with connection:
        connection.execute(READ_BOOK, (STATUS[True], book_id))


def remove_book(book_id: int):
    with connection:
        existing_ids = connection.execute(EXISTING_IDS).fetchall()
        if (book_id,) in existing_ids:
            connection.execute(DELETE_BOOK, (book_id,))
            return True
        else:
            return False
