from utils_files import database
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
            database.create_database()
            name = input("Escribe el nombre del libro: ").title()
            author = input("Escribe el autor del libro: ").title()
            database.add_book(name, author)

        elif user_input == 'l':
            pprint.pprint(database.all_books())

        elif user_input == 'r':
            name = input('Escribe el nombre del libro que has leído: ').title()
            database.book_status(name)

        elif user_input == 'd':
            pprint.pprint(database.all_books())
            while True:
                try:
                    book_id = int(input('Ingresa el ID del libro que deseas eliminar: '))
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
