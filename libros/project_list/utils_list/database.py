# pro y contra de usar como bases de datos listas/dict de python
# y compararlo con archivos csv, json, txt
# y luego compararlo con sql

books = []


def book_structure(name: str, author: str, status: bool) -> dict:
    return {'name': name, 'author': author, 'status': status}


def add_book(name: str, author: str) -> bool:
    book = book_structure(name, author, False)
    if book not in books:
        books.append(book)
        return True
    return False


def delete_book(name: str) -> None:
    global books
    books = [book for book in books if book.get('name') != name]
    # variable creada dentro de la función que itera sobre ella misma
    # python asume que es una variable local, por lo que necesitamos ese 'global'


def book_status(name: str, author: str) -> None:
    global books
    books = [
        book_structure(name, author, True) if book.get('name') == name and book.get('author') == author else book
        for book in books]
