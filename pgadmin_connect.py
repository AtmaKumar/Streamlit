import streamlit as st
#pip install psycopg2
import psycopg2
import pandas as pd


# Initialize connection.
# Uses st.experimental_singleton to only run once.
@st.experimental_singleton
def init_connection():
    return psycopg2.connect(**st.secrets["postgres"])

conn = init_connection()

# Perform query.
# Uses st.experimental_memo to only rerun when the query changes or after 10 min.
@st.experimental_memo(ttl=600)
def run_query(query):
    with conn.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()

rows = run_query("SELECT * from city limit 20")

data=pd.DataFrame(rows)
data.columns=['city_id','city','county_id','last_update']
st.table(data)
