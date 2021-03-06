CREATE_TABLE = """CREATE TABLE IF NOT EXISTS library (
    id INTEGER NOT NULL UNIQUE, 
    title TEXT NOT NULL, 
    author TEXT NOT NULL, 
    status NUMERIC,
    PRIMARY KEY(id AUTOINCREMENT)
);"""

INSERT_BOOK = "INSERT INTO library (title, author, status) VALUES (?, ? , ?);"

SHOW_ALL_BOOKS = "SELECT * FROM library;"

DELETE_BOOK = "DELETE FROM library WHERE id = ?;"

READ_BOOK = "UPDATE library SET status = ? WHERE id = ? LIMIT 1"

EXISTING_BOOKS = "SELECT title, author FROM library WHERE title = ? AND author = ? LIMIT 1;"

EXISTING_IDS = "SELECT id FROM library;"
