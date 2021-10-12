from datetime import datetime
import streamlit as st
import sqlite3

# ----- QUERIES -------
CREATE_TABLE = """CREATE TABLE IF NOT EXISTS posts (
    post_id INTEGER NOT NULL UNIQUE,
    post_author TEXT NOT NULL,
    post_title TEXT NOT NULL,
    post_len INTEGER NOT NULL,
    post_date TEXT NOT NULL,
    PRIMARY KEY (post_id AUTOINCREMENT))"""

INSERT_POST_INFO = "INSERT INTO posts (post_author, post_title, post_len, post_date) VALUES (?,?,?,?);"

SELECT_RECENT_POSTS = "SELECT post_date FROM posts ORDER BY post_id DESC LIMIT 5;"

# ------- FUNCTIONS --------
connection = sqlite3.connect('rebeca_blog_database.db')


def create_database():
    """
    This function creates the database if it does not exists.
    """
    with connection:
        connection.execute(CREATE_TABLE)


def add_post(author: str, title: str, post_len: str, date: str):
    char_len = len(post_len)
    print(char_len)
    with connection:
        connection.execute(INSERT_POST_INFO, (author, title, char_len, date))


def select_recent_posts() -> list[tuple]:
    """
    This function returns a list of tuples with the date of the last added posts.
    """
    with connection:
        return connection.execute(SELECT_RECENT_POSTS).fetchall()


# ---------- STREAMLIT ---------

def main():
    menu = ['Home', 'View Posts', 'Add Posts', 'Search', 'Manage Blog']
    choice = st.sidebar.selectbox('Menu', menu)
    create_database()
    if choice == 'Home':
        st.subheader('Home')
    elif choice == 'View Posts':
        recent_posts = []
        for x in select_recent_posts():
            for y in x:
                recent_posts.append(y) # no pude hacerlo por secuencias de comprensión. preguntar
        st.sidebar.selectbox('View Posts', recent_posts)

    elif choice == 'Add Posts':
        st.subheader('Add Articles')
        author = st.text_input('Enter Author\'s Name:', max_chars=50).title()
        post_title = st.text_input('Enter Post Title:')
        article = st.text_area('Post Article here:', height=50)
        date = st.text_input('Date:', datetime.now().strftime("%Y/%m/%d "))

        if st.button('Add'):
            add_post(author, post_title, article, date)
            st.success('The post was added successfully!')

    elif choice == 'Search':
        pass
    else:
        pass


if __name__ == '__main__':
    main()
