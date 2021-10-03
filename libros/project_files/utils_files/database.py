import csv
import os
from typing import Union

books_path = 'books.csv'

STATUS = {
    False: 'No leído',
    True: 'Leído',
}


def data_structure(book_id: Union[str, int], name: str, author: str, status: bool):
    return {
        'ID': book_id,
        'name': name,
        'author': author,
        'status': STATUS[status]
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
    check = [data_structure(str(index + 1), name, author, status) in books_list for status in (True, False)
             for index, _ in enumerate(books_list)]
    if not any(check):
        book_id = len(books_list) + 1
        with open(books_path, 'a', newline='', encoding='utf-8') as database:
            books_database = csv.DictWriter(database, ['ID', 'name', 'author', 'status'])
            books_database.writerows([data_structure(book_id, name, author, False)])
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
