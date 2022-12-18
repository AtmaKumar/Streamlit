import streamlit as st

Books = st.slider('How Many books you have read in a year?', 0,10)

st.write("I read ", Books, 'Books in a year')