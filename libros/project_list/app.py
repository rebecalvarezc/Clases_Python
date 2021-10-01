from utils_list import database

USER_OPTIONS = '''
- Introduce "a" para agregar un nuevo libro.
- Introduce "l" para mostrar todos los libros.
- Introduce "r" para marcar un libro como leído.
- Introduce "d" para eliminar un libro de la base de datos.
- Introduce "q" para salir.

Tu opción: --> '''  # formato menú


def menu():
    condicion = True

    while condicion:
        user_input = input(USER_OPTIONS)
        # Dependiendo de lo que se escoja hay que redirigirlo a donde va

        if user_input == 'a':
            name = input("Escribe el nombre del libro: ").lower()
            author = input("Escribe el autor del libro: ").lower()
            database.add_book(name, author)

        elif user_input == 'l':
            print(database.books)

        elif user_input == 'r':
            name = input('Escribe el nombre del libro que has leído: ').lower()
            database.book_status(name)

        elif user_input == 'd':
            name = input('Ingresa el nombre del libro que deseas eliminar: ')
            database.delete_book(name)

        elif user_input == 'q':
            print('Hasta pronto :)')
            condicion = False

        else:
            print('Ha introducido una opción incorrecta. Vuelva a intentarlo :)\n')


if __name__ == '__main__':
    menu()
