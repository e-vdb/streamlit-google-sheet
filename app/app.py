# streamlit_app.py

import streamlit as st
from gsheetsdb import connect

# Create a connection object.
conn = connect()

# Perform SQL query on the Google Sheet.
# Uses st.cache to only rerun when the query changes or after 10 min.
@st.cache(ttl=600)
def run_query(query):
    rows = conn.execute(query, headers=1)
    return rows

sheet_url = st.secrets["public_gsheets_url"]

def show_content(sheet_url):
    st.markdown("## Content of the google sheet")
    rows = run_query(f'SELECT * FROM "{sheet_url}"')
    for row in rows:
        st.write(f"{row.name} has a :{row.pet}:")

st.header("Streamlit web application: connection to public google sheet")
show_content(sheet_url)