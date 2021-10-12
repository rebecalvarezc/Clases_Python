from datetime import datetime
import sqlite3
from queries import *

connection = sqlite3.connect('rebeca_blog_database.db')
cursor = connection.cursor()


def create_database():
    """
    This function creates the database if it does not exists.
    """
    with connection:
        connection.execute(CREATE_TABLE)


def add_post(author: str, title: str, post_len: str, date: str):
    char_len = len(post_len)
    print(char_len)
    with cursor:
        cursor.execute(INSERT_POST_INFO, (author, title, char_len, date))
