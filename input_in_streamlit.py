import streamlit as st
name=st.text_input('Name')
age=st.number_input("Age")
date=st.date_input("Date")
file=st.file_uploader("select a file")

st.write(name)
st.write(age)
st.write(date)
if file is not None:
    a=file.getvalue()
    st.write(a)
