import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
data=pd.read_csv('data1.csv')
st.write(data.head())
data=data.iloc[:,:2]
st.write(data.head())

fig = px.pie(data, values='Prod_A', names='Week', title='Test')
st.plotly_chart(fig, use_container_width=True)