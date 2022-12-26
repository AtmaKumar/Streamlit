import streamlit as st
x=open('What is Streamlit.mp4','rb')
vi=x.read()
st.video(vi)