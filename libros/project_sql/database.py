import sqlite3
import database_queries

STATUS = {True: 'Leído', False: 'No leído'}

connection = sqlite3.connect('rebeca_library.db')


def create_library():
    """
    Función usada para crear la tabla de datos si no existe previamente.
    """
    with connection:
        connection.execute(database_queries.CREATE_TABLE)


def add_book(title: str, author: str, status: bool = STATUS[False]) -> bool:
    """
    Función usada para agregar el libro a las filas de la tabla de datos, siempre que este no exista previamente."
    """
    with connection:
        book_list = connection.execute(database_queries.EXISTING_BOOKS, (title, author)).fetchone()
        if book_list is None:
            connection.execute(database_queries.INSERT_BOOK, (title, author, status))
            return True
        return False


def show_books() -> list[tuple]:
    """
    Función usada para mostrar todos los libros de la tabla de datos.
    """
    with connection:
        return connection.execute(database_queries.SHOW_ALL_BOOKS).fetchall()


def change_book_status(book_id: int) -> bool:
    """
    Función utilizada para cambiar el valor en el status del libro dado.
    """
    with connection:
        existing_ids = connection.execute(database_queries.EXISTING_IDS).fetchall()
        if (book_id,) in existing_ids:
            connection.execute(database_queries.READ_BOOK, (STATUS[True], book_id))
            return True
        return False


def remove_book(book_id: int):
    """
    Función utilizada para eliminar un libro y su información de la base de datos.
    """
    with connection:
        existing_ids = connection.execute(database_queries.EXISTING_IDS).fetchall()
        if (book_id,) in existing_ids:
            connection.execute(database_queries.DELETE_BOOK, (book_id,))
            return True
        return False
