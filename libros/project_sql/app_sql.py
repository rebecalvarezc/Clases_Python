from libros.project_sql import database
import pprint
import os

os.system('cls')
USER_OPTIONS = '''
- Introduce "a" para agregar un nuevo libro.
- Introduce "l" para mostrar todos los libros.
- Introduce "r" para marcar un libro como leído.
- Introduce "d" para eliminar un libro de la base de datos.
- Introduce "q" para salir.

Tu opción: --> '''


def menu():
    connection = database.connect()
    database.create_library(connection)
    # while (user_input := input(USER_OPTIONS)) != "q":
    user_input = input(USER_OPTIONS)
    os.system('cls')
    if user_input == 'a':
        title = input("Escribe el nombre del libro: ").title()
        author = input("Escribe el autor del libro: ").title()
        database.add_book(connection, title, author)

    elif user_input == 'l':
        pprint.pprint(database.show_books(connection))

    else:
        pass
