import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from components.mngr_stores_sales_graph import mngr_stores_sales_graph
from components.mngr_vendors_sales_graph import mngr_vendors_sales_graph
from components.mngr_vendors_sales_circle_graph import mngr_vendors_sales_circle_graph
from components.goal import goal
import requests

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

# Function to fetch store sales data
def fetch_store_sales_data():
    query = """
    SELECT 
        toMonth(CAST(JSONExtractString(data, 'data') AS Date)) AS month, 
        JSONExtractString(data, 'cod_loja') AS store_name, 
        SUM(CAST(JSONExtractFloat(data, 'preco') AS Float64) * CAST(JSONExtractFloat(data, 'quantidade') AS Float64)) AS total_sales 
    FROM grupox 
    WHERE tag = 'transactions'
    GROUP BY month, store_name 
    ORDER BY month
    """
    data = query_clickhouse(query)
    if not data:
        return pd.DataFrame()

    # Convert the result into a pandas DataFrame
    df = pd.DataFrame(data, columns=['month', 'store_name', 'total_sales'])

    # Extract the region part from the store name (i.e., the first part before the "_")
    df['region'] = df['store_name'].str.extract(r'^([a-z]+(?:\s[a-z]+)?)', expand=False)

    return df

# Function to fetch vendor sales data for a specific store
def fetch_vendor_sales(selected_store):
    query = f"""
    SELECT 
        JSONExtractString(data, 'cod_vendedor') AS vendor_code,
        SUM(CAST(JSONExtractFloat(data, 'preco') AS Float64) * CAST(JSONExtractFloat(data, 'quantidade') AS Float64)) AS total_sales 
    FROM grupox 
    WHERE tag = 'transactions' AND JSONExtractString(data, 'cod_loja') = '{selected_store}'
    GROUP BY vendor_code
    ORDER BY total_sales DESC
    """
    data = query_clickhouse(query)
    if not data:
        return pd.DataFrame()

    df_vendors = pd.DataFrame(data, columns=['vendor_code', 'total_sales'])
    df_vendors['rank'] = df_vendors['total_sales'].rank(ascending=False, method='min').astype(int)

    return df_vendors

# Function to calculate goals dynamically
def calculate_goals(sales_data, selected_store=None):
    # Filter the sales data for the selected store, or keep all data if no store is selected
    if selected_store:
        filtered_data = sales_data[sales_data['store_name'] == selected_store]
    else:
        filtered_data = sales_data

    # Ensure there is data to work with
    if filtered_data.empty:
        return 0, 0

    # Group by month and calculate total sales per month
    monthly_sales = filtered_data.groupby('month').agg(total_sales=('total_sales', 'sum')).reset_index()

    # Sort by month (latest last)
    monthly_sales.sort_values('month', inplace=True)

    # Calculate Meta Mensal: last month's total sales + one-third of it
    if len(monthly_sales) > 0:
        last_month_sales = monthly_sales.iloc[-1]['total_sales']
        meta_mensal = round(last_month_sales + (last_month_sales / 3), 2)
    else:
        meta_mensal = 0

    # Calculate Meta Quinzenal: median of the last 3 months + one-third of it
    if len(monthly_sales) >= 3:
        last_three_months_sales = monthly_sales.iloc[-3:]['total_sales']
        median_last_three_months = last_three_months_sales.median()
        meta_quinzenal = round(median_last_three_months + (median_last_three_months / 3), 2)
    else:
        meta_quinzenal = 0

    return meta_mensal, meta_quinzenal

# Function to calculate the actual current sales value
def calculate_current_sales(sales_data, selected_store=None):
    # Filter the sales data for the selected store, or keep all data if no store is selected
    if selected_store:
        filtered_data = sales_data[sales_data['store_name'] == selected_store]
    else:
        filtered_data = sales_data

    # Ensure there is data to work with
    if filtered_data.empty:
        return 0

    # Sum the total sales for the current month (or total available data)
    total_sales = filtered_data['total_sales'].sum()

    return round(total_sales, 2)  # Round the total sales

# Updated mngr_stores_sales_graph function to handle both region and store-level grouping
def mngr_stores_sales_graph(data, title, group_by='region'):
    if group_by == 'region':
        # Group by month and region
        df_grouped = data.groupby(['month', 'region']).agg(total_sales=('total_sales', 'sum')).reset_index()

        # Pivot the DataFrame to get regions as columns and months as index
        df_pivoted = df_grouped.pivot(index='month', columns='region', values='total_sales')

    elif group_by == 'store':
        # Group by month and store
        df_grouped = data.groupby(['month', 'store_name']).agg(total_sales=('total_sales', 'sum')).reset_index()

        # Pivot the DataFrame to get stores as columns and months as index
        df_pivoted = df_grouped.pivot(index='month', columns='store_name', values='total_sales')

    df_pivoted.fillna(0, inplace=True)  # Fill any missing values with 0

    # Create plotly graph
    fig = go.Figure()

    cores = ['#E69F00', '#56B4E9', '#009E73', '#F0E442', '#0072B2', '#D55E00', '#CC79A7', '#000000']
    line_styles = ['solid', 'dash', 'dot', 'dashdot']

    for i, col in enumerate(df_pivoted.columns):
        cor = cores[i % len(cores)]
        style = line_styles[i // len(cores) % len(line_styles)]
        fig.add_trace(go.Scatter(
            x=df_pivoted.index,  # This is the 'month' index
            y=df_pivoted[col],
            name=col,
            line=dict(width=3, color=cor, dash=style)
        ))

    fig.update_layout(
        title=title,
        xaxis_title="Mês",
        yaxis_title="Valor Total de Vendas",
        legend_title="Regiões" if group_by == 'region' else "Lojas",
        hovermode="x unified",
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(
            family="Arial",
            size=14,
            color='white',
            weight='bold')
    )

    st.plotly_chart(fig)

# Enhanced goal function to handle division by zero and format the numbers
def goal(label, target, total, date):
    target = round(target, 2)
    total = round(total, 2)
    
    if total == 0:
        delta = "N/A"
    else:
        delta = f"{((target * 100) / total):.1f}%"

    st.metric(label=label, value=f"{target} / {total}", delta=delta)

# Main Dashboard Code
if st.session_state['role'] == "manager":
    # Page title
    st.title(f"Dashboard - {st.session_state['store']}")

    # Fetching sales data
    sales_data = fetch_store_sales_data()

    # Add selection for region or store-level visualization
    selected_region = st.selectbox('Selecione uma região para detalhar as lojas:', ['Todas'] + sorted(sales_data['region'].unique()), key="region_select")
    
    if selected_region == 'Todas':
        # Stores sales comparison by region
        st.subheader("Vendas por Região")
        mngr_stores_sales_graph(data=sales_data, title="Comparação entre Regiões", group_by='region')
    else:
        # Filter data for the selected region
        filtered_data = sales_data[sales_data['region'] == selected_region]

        # Add selection for specific stores within the region with a unique key to avoid DuplicateWidgetID error
        selected_store = st.selectbox(
            f'Selecione uma loja na região {selected_region}:', 
            ['Todas'] + sorted(filtered_data['store_name'].unique()),
            key=f"store_select_{selected_region}"
        )
        
        # Calculate dynamic goals
        meta_mensal, meta_quinzenal = calculate_goals(filtered_data if selected_store == 'Todas' else filtered_data[filtered_data['store_name'] == selected_store], selected_store)

        # Calculate current sales value
        current_sales = calculate_current_sales(filtered_data if selected_store == 'Todas' else filtered_data[filtered_data['store_name'] == selected_store])

        col1, col2 = st.columns([3, 3])
        # Goal 1: fifteen days
        with col1:
            goal("Meta de vendas mensal media", current_sales, meta_quinzenal, "15/10/2024")
        
        # Goal 2: monthly
        with col2:
            goal("Meta de vendas trimestal media", current_sales, meta_mensal, "15/10/2024")

        if selected_store == 'Todas':
            st.subheader(f"Vendas por Lojas na Região: {selected_region}")
            mngr_stores_sales_graph(data=filtered_data, title=f"Comparação entre Lojas da Região {selected_region}", group_by='store')
        else:
            st.subheader(f"Vendas da Loja: {selected_store}")
            mngr_stores_sales_graph(data=filtered_data[filtered_data['store_name'] == selected_store], title=f"Vendas da Loja {selected_store}", group_by='store')

            # Fetch vendor sales data for the selected store
            vendor_sales_data = fetch_vendor_sales(selected_store)

            if not vendor_sales_data.empty:
                # Define the meta for vendors
                vendor_meta = 115
                
                # Filter out vendors that did not exceed the meta
                vendors_above_meta = vendor_sales_data[vendor_sales_data['total_sales'] > vendor_meta]
                
                # Check if any vendors exceeded the meta
                if not vendors_above_meta.empty:
                    st.subheader("Vendedores que ultrapassaram a meta este mês")

                    # Prepare data for the bar graph
                    vendor_sales = {
                        'Categorias': vendors_above_meta['vendor_code'].tolist(),
                        'Valores': vendors_above_meta['total_sales'].tolist(),
                        'Cores': ['#56B4E9', '#009E73', '#F0E442', '#0072B2'][:len(vendors_above_meta)]  # Adjust color list
                    }

                    col1, col2 = st.columns([5, 5])
                    
                    # Display the bar graph
                    with col1:
                        mngr_vendors_sales_graph(data_vendedores=vendor_sales, title="Ranking de Vendedores", meta=vendor_meta)
                    
                    # Display the sales circle graph (donut chart)
                    with col2:
                        mngr_vendors_sales_circle_graph(data_vendedores=vendor_sales, title="Participação nas Vendas")
                else:
                    st.write("Nenhum vendedor ultrapassou a meta este mês.")

            else:
                st.write("Nenhum dado de vendas encontrado para essa loja.")
