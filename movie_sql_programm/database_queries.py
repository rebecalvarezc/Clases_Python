CREATE_MOVIE_TABLE = """ CREATE TABLE IF NOT EXISTS movies (
    movie_id  INTEGER NOT NULL UNIQUE,
    title TEXT NOT NULL,
    release_timestamp REAL NOT NULL,
    PRIMARY KEY(movie_id AUTOINCREMENT)
);"""

CREATE_USER_TABLE = """ CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER NOT NULL UNIQUE,
    watcher_name TEXT NOT NULL,
    watcher_last_name TEXT NOT NULL,
    username TEXT NOT NULL,
    PRIMARY KEY (user_id AUTOINCREMENT)
);"""

CREATE_WATCHED_TABLE = """ CREATE TABLE IF NOT EXISTS watched_movies (
    user_id NOT NULL,
    movie_id TEXT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users, 
    FOREIGN KEY (movie_id) REFERENCES movies
);"""


CHECK_MOVIE = "SELECT title, release_timestamp FROM movies WHERE title = ? AND release_timestamp = ? LIMIT 1;"

INSERT_MOVIE = "INSERT INTO movies (title, release_timestamp) VALUES (?, ?);"

SHOW_MOVIES = "SELECT movie_id, title, release_timestamp FROM movies;"

UPCOMING_MOVIES = "SELECT movie_id, title, release_timestamp FROM movies WHERE release_timestamp > ?;"

USERS_IDS = "SELECT user_id FROM users WHERE username = ? LIMIT 1;"

MOVIES_IDS = "SELECT title FROM movies WHERE movie_id = ? LIMIT 1;"

WATCHED_MOVIE = ""

ADD_USER = "INSERT INTO users(watcher_name, watcher_last_name, username) VALUES (?,?,?);"



