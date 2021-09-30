# pro y contra de usar como bases de datos listas/dict de python
# y compararlo con archivos csv, json, txt
# y luego compararlo con sql

books = []


def add_book(name: str, author: str):
    books.append({'name': name, 'author': author, 'status': False})  # Este false se cambia con 'r'


def delete_book(name: str):
    i = 0
    for book in books:
        if book.get('name') == name:
            books.pop(i)
        else:
            i += 1


def book_status(name: str):
    for book in books:
        if book.get('name') == name:
            book['status'] = True
        else:
            print('Ese libro no se encuentra en la lista.')
