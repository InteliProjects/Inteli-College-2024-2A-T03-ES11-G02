import streamlit as st
import requests
import json

# Base URL for the Flask API
FLASK_API_URL = "http://localhost:5000"

# Function to query ClickHouse via Flask API
def query_clickhouse(query):
    try:
        response = requests.post(f"{FLASK_API_URL}/clickhouse/query", json={"query": query})
        if response.status_code == 200:
            return response.json()
        else:
            st.error(f"Error querying ClickHouse: {response.json().get('error')}")
            return []
    except requests.exceptions.RequestException as e:
        st.error(f"Connection error: {e}")
        return []

# Main function for Data Builder page

st.title("ClickHouse Data Viewer")

# Input field for custom SQL query
query = st.text_input("Enter your ClickHouse query", "SELECT * FROM grupox LIMIT 100")

if st.button("Run Query"):
    st.write("Fetching data from ClickHouse...")
    data = query_clickhouse(query)
    
    if data:
        st.write("Data loaded successfully!")
        st.dataframe(data)
    else:
        st.write("No data returned or an error occurred.")
