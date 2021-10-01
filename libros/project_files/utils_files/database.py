import csv

books = []


def add_book(name: str, author: str):
    books.append({'name': name, 'author': author, 'status': False})
    with open('books.txt', 'a', newline='') as database:
        books_database = csv.DictWriter(database, ['name', 'author', 'status'])
        books_database.writeheader()
        books_database.writerows(books)
        # Preguntar Rodney


def delete_book(name: str):
    global books
    books = [book for book in books if book.get('name') != name]
    with open('books.txt', 'w', newline='') as database:
        books_database = csv.DictWriter(database, ['name', 'author', 'status'])
        books_database.writeheader()
        books_database.writerows(books)


def book_status(name: str):
    # global books
    # books = [book['status'] = True for book in books if book.get('name') == name]  # Preguntar a Rodney
    for book in books:
        if book.get('name') == name:
            book['status'] = True

    with open('books.txt', 'w', newline='') as database:
        books_database = csv.DictWriter(database, ['name', 'author', 'status'])
        books_database.writeheader()
        books_database.writerows(books)
    # como hacer para que si no encuentra el libro me avise?
