# pro y contra de usar como bases de datos listas/dict de python
# y compararlo con archivos csv, json, txt
# y luego compararlo con sql

books = []


def add_book(name: str, author: str) -> bool:
    book = {'name': name, 'author': author, 'status': False}
    if book not in books:
        books.append(book)  # Este false se cambia con 'r'
        return True
    return False


def delete_book(name: str):
    global books
    books = [book for book in books if book.get('name') != name]
    # variable creada dentro de la función que itera sobre ella misma
    # python asume que es una variable local, por lo que necesitamos ese 'global'


def book_status(name: str) -> bool:
    # Practica: buscar llevar esta función a dos lineas de código o una.

    for book in books:
        if book.get('name') == name:
            book['status'] = True
            return True  # El return funciona como un break
    return False
