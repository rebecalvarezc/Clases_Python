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
    book_false = {'name': name, 'author': author, 'status': STATUS[False]}
    book_true = {'name': name, 'author': author, 'status': STATUS[True]}
    if book_false or book_true in books_list:
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


# pendiente
def book_status(name: str) -> bool:
    books_list = all_books()
    for book in books_list:
        if book.get('name') == name:
            book['status'] = True
            with open(books_path, 'w', newline='', encoding='utf-8') as database:
                books_database = csv.DictWriter(database, ['ID', 'name', 'author', 'status'])
                books_database.writeheader()
                books_database.writerows(books_list)
            return True
    return False
