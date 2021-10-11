import datetime
import time
from PIL import Image
import streamlit as st

# title
st.title('Hi, welcome!')
# header
st.header('Rebeca\'s Webpage')
# subheader
st.subheader('hi human')
# text
st.text('what brings you to my domain?')
# markdown
st.markdown('### Castle')
# success
st.success('Successfully done')
# error
st.error('WHAT ARE YOU DOING?!')
# info
st.info('Be careful and read this -.-')
# warning
st.warning('DONT YOU DARE TOUCH THIS')
# exceptions
# st.exception(ValueError)
# help functions
st.help(range)
# check box
if st.checkbox('Show/Hide'):
    st.write('You did it.')
# radio buttons
status = st.radio('What is your status?', ('active', 'inactive'))
if status == 'active':
    st.success('Well done, you human')
else:
    st.warning('Go grab some coffee.')
# select box
career = st.selectbox('Whats your profession?', ('doctor', 'programmer', 'stripper'))
st.text(f'You selected: {career}')
# multiselect
place = st.multiselect('Where do you work?', ('Hogwarts', 'Narnia', 'One Piece'))
st.write(f'Wow, you work in {place}?')
# slider
age = st.slider('Your age: ', 18, 100)
st.write(f'Are you {age} years old?')
# buttons
st.button('DON\'T CLICK')
if st.button('Touch me :)'):
    st.write('You naughty human!')
# inputs
secret = st.text_input('Tell me a secret: ')
if st.button('Submit'):
    st.success(f'Your secret is safe with me! You wrote: {secret}')
# descripciones
st.text_area('Please, don\'t write too much.')
# entradas fecha
st.date_input('The date is: ', datetime.datetime.now())
st.time_input('The time is: ', datetime.time())  # desplegable con el tiempo
mariana = {
    "name": "Mariana",
    "age": 25,
    "status": "cousin"
}
st.text('Display json: ')
st.json(mariana)
# st.balloons()
bar = st.progress(0)
# for i in range(100):
# bar.progress(i+1)
# time.sleep(0.3)
# spinner
# with st.spinner('In progress...'):
#     time.sleep(5)
#     st.success('Done')
# side bar
st.sidebar.header('About: ')
st.sidebar.text('This is a try out page, go away.')
img = Image.open('babylights.jpg')
st.image(img, width=300, caption='Highlights')  # se puede poner videos y audios también

st.code('lambda x, y: x + y')  # lambda = def
st.button('Hit me')
st.download_button('On the dl', str([1, 2, 3]))
st.checkbox('Check me out')
st.radio('Radio', [1,2,3])
st.selectbox('Select', [1,2,3])
st.multiselect('Multiselect', [1,2,3])
st.slider('Slide me', min_value=0, max_value=10)
st.select_slider('Slide to select', options=[1,'2'])
st.text_input('Enter some text')
st.number_input('Enter a number')
st.text_area('Area for textual entry')
st.date_input('Date input')
st.time_input('Time entry')
st.file_uploader('File uploader')
color = st.color_picker('Pick a color')
st.write(color)

st.echo()
with st.echo():
    st.write('A + B = C')