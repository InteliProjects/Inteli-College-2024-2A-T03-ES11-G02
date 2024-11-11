import streamlit as st
import pandas as pd
from st_aggrid import AgGrid
from st_aggrid.grid_options_builder import GridOptionsBuilder
import requests
import json
from datetime import datetime

# Base URL for the Flask API
FLASK_API_URL = "http://localhost:5000"

# Function to query ClickHouse via Flask API
def query_clickhouse(query):
    try:
        response = requests.post(f"{FLASK_API_URL}/clickhouse/query", json={"query": query})
        if response.status_code == 200:
            return response.json()  # Assuming the data is returned in JSON format
        else:
            st.error(f"Error querying ClickHouse: {response.json().get('error')}")
            return []
    except requests.exceptions.RequestException as e:
        st.error(f"Connection error: {e}")
        return []

# Function to convert parsed JSON data into a DataFrame
def convert_json_to_table(data):
    rows = []
    for item in data:
        try:
            row = {
                'ID': item[0] if len(item) > 0 else None,  # cod_transacao
                'VENDEDOR': item[1] if len(item) > 1 else None,  # cod_vendedor
                'LOJA': item[2] if len(item) > 2 else None,  # cod_loja
                'DATA': item[5] if len(item) > 5 else None,  # transaction_date
                'PREÇO': item[3] if len(item) > 3 else None,  # preco
                'QUANTIDADE': item[4] if len(item) > 4 else None  # quantidade
            }
            rows.append(row)
        except (KeyError, TypeError, json.JSONDecodeError) as e:
            st.error(f"Error parsing data: {e}")
            continue
    return pd.DataFrame(rows)

# Check authentication status before rendering the page
if 'authentication_status' not in st.session_state or st.session_state["authentication_status"] == False:
    st.switch_page('pages/login.py')
else:
    st.title("Transações")

    # Add date range filter
    today = datetime.today()
    start_date = st.date_input("Start date", value=today.replace(month=1, day=1))  # Default to the beginning of the current year
    end_date = st.date_input("End date", value=today, max_value=today)  # Default to today with today as max value

    if start_date > end_date:
        st.error("Start date must be before the end date.")
    else:
        # Query ClickHouse for transaction data within the selected date range
        query_transactions = f"""
        SELECT 
            JSONExtractString(data, 'cod_transacao') AS cod_transacao,
            JSONExtractString(data, 'cod_loja') AS cod_loja,
            JSONExtractFloat(data, 'preco') AS preco,
            JSONExtractString(data, 'cod_vendedor') AS cod_vendedor,
            JSONExtractUInt(data, 'quantidade') AS quantidade,
            JSONExtractString(data, 'data') AS transaction_date
        FROM grupox
        WHERE tag = 'transactions'
        AND JSONExtractString(data, 'data') BETWEEN '{start_date}' AND '{end_date}'
        LIMIT 10000
        """

        transactions_data_raw = query_clickhouse(query_transactions)
        transactions_data = convert_json_to_table(transactions_data_raw) if transactions_data_raw else pd.DataFrame()

        if not transactions_data.empty:
            # Build grid options with responsive width
            gd = GridOptionsBuilder.from_dataframe(transactions_data)
            gd.configure_pagination(enabled=True)
            gd.configure_default_column(editable=True, groupable=True)
            sel_mode = st.radio('SelectionType', options=['single', 'multiple'], index=0)
            gd.configure_selection(selection_mode=sel_mode, use_checkbox=True)
            gridoptions = gd.build()

            # Adjust grid options for full width and responsive layout
            AgGrid(transactions_data, gridOptions=gridoptions, height=500, fit_columns_on_grid_load=True, theme="streamlit", width='100%')
        else:
            st.write("No transaction data available for the selected date range.")
