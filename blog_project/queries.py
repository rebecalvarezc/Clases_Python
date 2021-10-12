CREATE_TABLE = """CREATE TABLE IF NOT EXISTS posts (
    post_id INTEGER NOT NULL UNIQUE,
    post_author TEXT NOT NULL,
    post_title TEXT NOT NULL,
    post_len INTEGER NOT NULL,
    post_date TEXT NOT NULL,
    PRIMARY KEY (post_id AUTOINCREMENT))"""

INSERT_POST_INFO = "INSERT INTO posts (post_author, post_title, post_len, post_date) VALUES (?,?,?,?)"