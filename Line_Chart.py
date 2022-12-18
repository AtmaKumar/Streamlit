import streamlit as st
import pandas as pd
data=pd.read_csv('data1.csv')
st.write(data.head())
data=data.iloc[:,1:]
st.write(data.head())
st.line_chart(data)