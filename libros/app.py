from utils import database

USER_OPTIONS = '''
- Introduce "a" para agregar un nuevo libro.
- Introduce "l" para mostrar todos los libros.
- Introduce "r" para marcar un libro como leído.
- Introduce "d" para eliminar un libro de la base de datos.
- Introduce "q" para salir.

Tu opción: --> '''  # formato menú


# ciclo hasta que presione q
# y si el usuario mete un valor incorrecto? --> While

def menu():
    while (user_input := input(USER_OPTIONS)) != "q":
        # Dependiendo de lo que se escoja hay que redirigirlo a donde va

        if user_input == 'a':
            name = input("Escribe el nombre del libro: ")
            author = input("Escribe el autor del libro: ")
            database.add_book(name, author)

        elif user_input == 'l':
            print(database.books)

        elif user_input == 'r':
            name = input('Escribe el nombre del libro que has leído: ')
            database.book_status(name)

        elif user_input == 'd':
            name = input('Ingresa el nombre del libro que deseas eliminar: ')
            database.delete_book(name)

        else:
            print("Por favor, ingresa un comendo válido!")


if __name__ == '__main__':
    menu()

# tarea: hacer el resto de funciones, que sea amigable.
