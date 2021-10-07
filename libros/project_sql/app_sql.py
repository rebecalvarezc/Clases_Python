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
    database.create_library()

    while (user_input := input(USER_OPTIONS)) != "q":
        os.system('cls')
        if user_input == 'a':
            title = input("Escribe el nombre del libro: ").title()
            author = input("Escribe el autor del libro: ").title()
            added = database.add_book(title, author)

            if added:
                print('\nSe ha agregado el libro satisfactoriamente!')
            else:
                print('\nEl libro ya existe en la base de datos!')

        elif user_input == 'l':
            pprint.pprint(database.show_books())

        elif user_input == 'r':
            pprint.pprint(database.show_books())
            book_id = int(input('Escribe el ID del libro que has leído: '))
            database.change_book_status(book_id)
            print(f'\nEl estado del libro de id: {book_id} ha cambiado a "Leído".')

        elif user_input == 'd':
            pprint.pprint(database.show_books())
            book_id = int(input('Ingresa el ID del libro que deseas eliminar: '))
            deleted = database.remove_book(book_id)

            if deleted:
                print('\nOperación realizada satisfactoriamente :)')
            else:
                print(f'\nNo se ha encontrado un libro con id {book_id}!')

        else:
            print("Por favor, ingresa un comando válido!")
    print('\nHasta pronto :)')


if __name__ == '__main__':
    menu()
