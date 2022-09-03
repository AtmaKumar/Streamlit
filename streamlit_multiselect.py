import streamlit as st


options = st.multiselect(
     'Select State',
     ['Delhi', 'UP', 'MP', 'Bihar'],
['Delhi'])

st.write(options)








