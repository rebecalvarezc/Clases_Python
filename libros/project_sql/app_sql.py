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

        elif user_input == 'l':
            pprint.pprint(database.show_books(connection))

        elif user_input == 'r':
            pprint.pprint(database.show_books(connection))
            book_id = input('Escribe el ID del libro que has leído: ').title()
            # funcion para cambiar el estado

        elif user_input == 'd':
            pprint.pprint(database.show_books(connection))
            while True:
                try:
                    book_id = input('Ingresa el ID del libro que deseas eliminar: ')
                    # funcion para eliminar
                    break
                except ValueError:
                    print('Escribe el ID del libro.')
                    continue
            print('Operación realizada satisfactoriamente :)')

        else:
            print("Por favor, ingresa un comando válido!")

    print('Hasta pronto :)')


if __name__ == '__main__':
    menu()
