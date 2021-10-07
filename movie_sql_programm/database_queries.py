# MOVIE QUERIES

CREATE_MOVIE_TABLE = """ CREATE TABLE IF NOT EXISTS movies (
    movie_id  INTEGER NOT NULL UNIQUE,
    title TEXT NOT NULL,
    release_timestamp REAL NOT NULL,
    watched NUMERIC NOT NULL,
    PRIMARY KEY(movie_id AUTOINCREMENT)
);"""

INSERT_MOVIE = "INSERT INTO movies (title, release_timestamp, watched) VALUES (?, ?, ?);"

SHOW_MOVIES = "SELECT movie_id, title, release_timestamp FROM movies ;"

UPCOMING_MOVIES = "SELECT movie_id, title, release_timestamp FROM movies WHERE release_timestamp > ?;"

# USER QUERIES

# CREATE_USER_TABLE = """ CREATE TABLE IF NOT EXISTS users (
#     watcher_name TEXT NOT NULL,
#     title REAL NOT NULL,
#     PRIMARY KEY (title)
# );"""

# JOIN_USER_MOVIE_TABLES = """SELECT users.*, movies.movie_id, movies.watched
#     FROM movies JOIN users ON users.title = movies.title """ # Preguntar Rodney
