import streamlit as st


x = st.radio('Are you a student',options=['Yes', 'No'], index=0)

if(x=="Yes"):
    st.write("Yes he is a student")
else:
    st.write("No he is not a student")







