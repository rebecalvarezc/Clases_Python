import json
import os

STATUS = {True: 'Leído', False: 'No leído'}

database_name = 'rebeca_library.json'


def create_database() -> None:
    if not os.path.exists(database_name):
        with open(database_name, 'w', encoding='utf-8') as file:
            json.dump([], file)  # arreglo vacío  # fp = file pointer


def save_all_books(books: list[dict]) -> None:
    with open(database_name, 'w', encoding='utf-8') as file:
        json.dump(books, file)


def open_library():
    with open(database_name, 'r', encoding='utf-8') as all_books:
        books = json.load(all_books)
    return books


def add_book(name: str, author: str):
    books = open_library()
    book_id = len(books) + 1
    book_exists = [{str(i): {'name': name, 'author': author, 'status': STATUS[_]}} in books for _ in (True, False)
                   for i in range(1, book_id)]
    if not any(book_exists):
        books.append({book_id: {'name': name, 'author': author, 'status': STATUS[False]}})
        save_all_books(books)
        return True
    return False


def book_status(book_id: str) -> bool:
    books = open_library()
    for book in books:
        if book.get(book_id):
            book[book_id]['status'] = STATUS[True]
            save_all_books(books)
            return True
    return False


def delete_book(book_id: str) -> None:
    books = open_library()
    books = [book for book in books if book_id not in book.keys()]
    save_all_books(books)
