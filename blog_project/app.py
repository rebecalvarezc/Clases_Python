from datetime import datetime
import streamlit as st
import global_functions as gf

st.header('Rebeca\'s Blog')


def main():
    menu = ['Home', 'View Posts', 'Add Posts', 'Search', 'Manage Blog']
    choice = st.sidebar.selectbox('Menu', menu)

    if choice == 'Home':
        pass
    elif choice == 'View Posts':
        pass
    elif choice == 'Add Posts':
        st.subheader('Add Articles')
        author = st.text_input('Enter Author\'s Name:', max_chars=50).title()
        post_title = st.text_input('Enter Post Title:')
        article = st.text_area('Post Article here:', height=50)
        date = st.text_input('Date:', datetime.now().strftime("%Y/%m/%d "))

        if st.button('Add'):
            gf.add_post(author, post_title, article, date)

    elif choice == 'Search':
        pass
    else:
        pass


if __name__ == '__main__':
    main()
