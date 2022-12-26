import streamlit as st
st.info('This is Data Science Page', icon="ℹ️")

st.warning('warning here,Pls Check', icon="⚠️")

st.error('an error here,Pls Check', icon="🚨")

st.success('success message,Great', icon="✅")


with st.spinner('Pls wait'):
    x=0
    while(x<30000000):
        x=x+1
st.success('Done!')


y = st.progress(0)
for percent_complete in range(100):
    while(x<60000000):
        x=x+1
    y.progress(percent_complete + 1)

