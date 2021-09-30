# pro y contra de usar como bases de datos listas/dict de python
# y compararlo con archivos csv, json, txt
# y luego compararlo con sql

books = []


def add_book(name: str, author: str):
    books.append({'name': name, 'author': author, 'status': False})  # Este false se cambia con 'r'


def delete_book(name: str):
    global books
    books = [book for book in books if
             book.get('name') != name]  # variable creada dentro de la función que itera sobre ella misma
    # python asume que es una variable local, por lo que necesitamos ese 'global'


def book_status(name: str):
    for book in books:
        if book.get('name') == name:
            book['status'] = True
        else:
            print(f'\nEl libro {name} no se encuentra en la base de datos.')
            break
