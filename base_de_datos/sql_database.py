# codigo de python asociado a la ejecución de todas las queries
import sqlite3
from db_queries import *

database_name = 'beans.db'


def connect():
    return sqlite3.connect(database_name)  # para ejecutar la conexión


def create_table(connection):
    with connection:
        connection.execute(CREATE_BEANS_TABLE)


def add_bean(connection, name: str, method: str, rating: int):
    with connection:
        connection.execute(INSERT_BEANS, (name, method, rating))


def gather_beans(connection):
    with connection:
        return connection.execute(GATHER_BEANS).fetchall()


def bean_name(connection, name: str):
    with connection:
        return connection.execute(GATHER_BEAN_NAME, (name,)).fetchall()


def best_bean(connection):
    with connection:
        return connection.execute(BEST_RATED_BEAN).fetchone()  # porque sé que estoy recibiendo uno solo.
