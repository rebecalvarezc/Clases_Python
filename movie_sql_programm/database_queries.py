# MOVIE QUERIES

CREATE_MOVIE_TABLE = """ CREATE TABLE IF NOT EXISTS movies (
    movie_id  INTEGER NOT NULL UNIQUE,
    title TEXT NOT NULL,
    release_timestamp REAL NOT NULL,
    watched NUMERIC NOT NULL,
    PRIMARY KEY(movie_id AUTOINCREMENT)
);"""

CHECK_MOVIE = "SELECT title, release_timestamp FROM movies WHERE title = ? AND release_timestamp = ? LIMIT 1;"

INSERT_MOVIE = "INSERT INTO movies (title, release_timestamp, watched) VALUES (?, ?, 0);"

SHOW_MOVIES = "SELECT movie_id, title, release_timestamp FROM movies;"

UPCOMING_MOVIES = "SELECT movie_id, title, release_timestamp FROM movies WHERE release_timestamp > ?;"

MOVIES_IDS = "SELECT title FROM movies WHERE movie_id = ? LIMIT 1;"

CHANGE_WATCHED_MOVIE = "UPDATE movies SET watched = 1, release_timestamp = ? WHERE movie_id = ?;"

WATCHED_MOVIES = "SELECT movie_id, title, release_timestamp FROM movies WHERE watched = 1;"

# USER QUERIES

# CREATE_USER_TABLE = """ CREATE TABLE IF NOT EXISTS users (
#     watcher_name TEXT NOT NULL,
#     title REAL NOT NULL,
#     PRIMARY KEY (title)
# );"""

# JOIN_USER_MOVIE_TABLES = """SELECT users.*, movies.movie_id, movies.watched
#     FROM movies JOIN users ON users.title = movies.title """ # Preguntar Rodney
