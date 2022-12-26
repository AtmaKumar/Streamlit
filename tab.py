import streamlit as st
tab1,tab2,tab3,tab4=st.tabs(['a','b','c','d'])
with tab1:
    st.write('India')
with tab2:
    st.write('Ballia')
with tab3:
    st.write('Delhi')
with tab4:
    st.write('Data Science')