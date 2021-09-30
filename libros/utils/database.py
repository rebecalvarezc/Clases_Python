# pro y contra de usar como bases de datos listas/dict de python
# y compararlo con archivos csv, json, txt
# y luego compararlo con sql

books = []


def add_book(name: str, author: str):
    books.append({'name': name, 'author': author, 'status': False})  # Este false se cambia con 'r'
