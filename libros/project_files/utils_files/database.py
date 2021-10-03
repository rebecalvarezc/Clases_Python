import csv
import os

books_path = 'books.csv'

STATUS = {
    False: 'No leído',
    True: 'Leído',
}


def create_database() -> None:
    if not os.path.exists('books.csv'):
        with open(books_path, 'w', newline='', encoding='utf-8') as database:
            books_database = csv.DictWriter(database, ['ID', 'name', 'author', 'status'])
            books_database.writeheader()


def all_books() -> list:
    with open(books_path, 'r', encoding='utf-8') as database:
        book_list = list(csv.DictReader(database))
    return book_list


def add_book(name: str, author: str) -> bool:
    books_list = all_books()
    check = [{'ID': str(i), 'name': name, 'author': author, 'status': STATUS[_]} in books_list for _ in (True, False)
             for i in range(1, len(books_list) + 1)]
    if not any(check):  # un diccionario solo es falso si no tiene información.
        book_id = len(all_books()) + 1
        with open(books_path, 'a', newline='', encoding='utf-8') as database:
            books_database = csv.DictWriter(database, ['ID', 'name', 'author', 'status'])
            books_database.writerows([{'ID': book_id, 'name': name, 'author': author, 'status': STATUS[False]}])
        return True
    return False


def delete_book(book_id: int) -> None:
    books = all_books()
    books = [book for book in books if int(book.get('ID')) != book_id]
    with open(books_path, 'w', newline='', encoding='utf-8') as database:
        books_database = csv.DictWriter(database, ['ID', 'name', 'author', 'status'])
        books_database.writeheader()
        books_database.writerows(books)


def book_status(book_id: str) -> bool:
    books_list = all_books()
    for book in books_list:
        if book.get('ID') == book_id:
            book['status'] = STATUS[True]
            with open(books_path, 'w', newline='', encoding='utf-8') as database:
                books_database = csv.DictWriter(database, ['ID', 'name', 'author', 'status'])
                books_database.writeheader()
                books_database.writerows(books_list)
            return True
    return False
