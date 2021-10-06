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

    while (user_input := input(USER_OPTIONS)) != "q":
        user_input = input(USER_OPTIONS)
        os.system('cls')
        if user_input == 'a':
            title = input("Escribe el nombre del libro: ").title()
            author = input("Escribe el autor del libro: ").title()
            database.add_book(connection, title, author)
            print('\nSe ha agregado el libro satisfactoriamente!')

        elif user_input == 'l':
            pprint.pprint(database.show_books(connection))

        elif user_input == 'r':
            pprint.pprint(database.show_books(connection))
            book_id = int(input('Escribe el ID del libro que has leído: '))
            database.change_book_status(connection, book_id)
            print(f'\nEl estado del libro de id: {book_id} ha cambiado a "Leído".')
        elif user_input == 'd':
            pprint.pprint(database.show_books(connection))
            book_id = int(input('Ingresa el ID del libro que deseas eliminar: '))
            database.remove_book(connection, book_id)
            print('\nOperación realizada satisfactoriamente :)')

    print('\nHasta pronto :)')


if __name__ == '__main__':
    menu()
