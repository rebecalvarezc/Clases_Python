import sqlite3

from libros.project_sql.database_queries import *

STATUS = {True: 'Leído', False: 'No leído'}

database_name = 'rebeca_library.db'


def connect():
    """
    Función usada para generar la conexión con la base de datos.
    """
    return sqlite3.connect(database_name)


def create_library(connection) -> None:
    """
    Función usada para crear la tabla de datos si no existe previamente.
    """
    with connection:
        connection.execute(CREATE_TABLE)


def add_book(connection, title: str, author: str, status: bool = STATUS[False]) -> bool:
    """
    Función usada para agregar el libro a las filas de la tabla de datos, siempre que este no exista previamente."
    """
    with connection:
        book_list = connection.execute(EXISTING_BOOKS, (title, author)).fetchall()
        if book_list is None:
            connection.execute(INSERT_BOOK, (title, author, status))
            return True
        return False


def show_books(connection) -> list[tuple]:
    """
    Función usada para mostrar todos los libros de la tabla de datos.
    """
    with connection:
        return connection.execute(SHOW_ALL_BOOKS).fetchall()


def change_book_status(connection, book_id: int) -> None:
    """
    Función utilizada para cambiar el valor en el status del libro dado.
    """
    with connection:
        connection.execute(READ_BOOK, (STATUS[True], book_id))


def remove_book(connection, book_id: int) -> bool:
    """
    Función utilizada para eliminar un libro y su información de la base de datos.
    """
    with connection:
        existing_ids = connection.execute(EXISTING_IDS).fetchall()
        if (book_id,) in existing_ids:
            connection.execute(DELETE_BOOK, (book_id,))
            return True
        return False
