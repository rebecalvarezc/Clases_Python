from utils_json import database
import pprint
import os
os.system('cls')
USER_OPTIONS = '''
- Introduce "a" para agregar un nuevo libro.
- Introduce "l" para mostrar todos los libros.
- Introduce "r" para marcar un libro como leído.
- Introduce "d" para eliminar un libro de la base de datos.
- Introduce "q" para salir.

Tu opción: --> '''  # formato menú


def menu():
    database.create_database()
    while (user_input := input(USER_OPTIONS)) != "q":
        os.system('cls')
        if user_input == 'a':
            name = input("Escribe el nombre del libro: ").title()
            author = input("Escribe el autor del libro: ").title()
            status = database.add_book(name, author)
            if not status:
                print('El libro que desea agregar ya existe en la base de datos!')

        elif user_input == 'l':
            pprint.pprint(database.open_library())

        elif user_input == 'r':
            pprint.pprint(database.open_library())
            book_id = input('Escribe el ID del libro que has leído: ').title()
            status = database.book_status(book_id)
            if not status:
                print('El libro indicado no se encuentra en la base de datos.')
            else:
                print(f'El libro se ha marcado como leído :)')

        elif user_input == 'd':
            pprint.pprint(database.open_library())
            while True:
                try:
                    book_id = input('Ingresa el ID del libro que deseas eliminar: ')
                    database.delete_book(book_id)
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
