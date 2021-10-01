from utils_list import database
import pprint

USER_OPTIONS = '''
- Introduce "a" para agregar un nuevo libro.
- Introduce "l" para mostrar todos los libros.
- Introduce "r" para marcar un libro como leído.
- Introduce "d" para eliminar un libro de la base de datos.
- Introduce "q" para salir.

Tu opción: --> '''  # formato menú


def menu():
    while (user_input := input(USER_OPTIONS)) != "q":
        if user_input == 'a':
            name = input("Escribe el nombre del libro: ")
            author = input("Escribe el autor del libro: ")
            status = database.add_book(name, author)
            if status:
                print('El libro se ha agregado satisfactoriamente!')
            else:
                print('El libro ya se encuentra en la base de datos.')

        elif user_input == 'l':
            pprint.pprint(database.books)

        elif user_input == 'r':
            name = input('Escribe el nombre del libro que has leído: ')
            state = database.book_status(name)
            if not state:
                print('\nEl libro no se encuentra en la base de datos.')
            else:
                print('\nSe ha cambiado el estado de su libro exitosamente!')

        elif user_input == 'd':
            name = input('Ingresa el nombre del libro que deseas eliminar: ')
            database.delete_book(name)

        else:
            print("Por favor, ingresa un comando válido!")

    print('Hasta pronto :)')


if __name__ == '__main__':
    menu()
