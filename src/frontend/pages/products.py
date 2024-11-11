import streamlit as st
import math
import requests

# Base URL for the Flask API
FLASK_API_URL = "http://localhost:5000"

# Function to query ClickHouse via Flask API
def query_clickhouse(query):
    try:
        response = requests.post(f"{FLASK_API_URL}/clickhouse/query", json={"query": query})
        if response.status_code == 200:
            return response.json()  # Assuming the data is returned as a list
        else:
            st.error(f"Error querying ClickHouse: {response.json().get('error')}")
            return []
    except requests.exceptions.RequestException as e:
        st.error(f"Connection error: {e}")
        return []

# Function to fetch all product data from sku_dataset (name, cod_prod, and nome_completo)
@st.cache_data
def fetch_product_details():
    query = """
    SELECT 
        JSONExtractString(data, 'cod_prod') AS cod_prod,
        JSONExtractString(data, 'nome_abrev') AS nome_abrev,
        JSONExtractString(data, 'nome_completo') AS nome_completo
    FROM grupox
    WHERE tag = 'sku_dataset'
    """
    return query_clickhouse(query)

# Function to fetch all products and related products with pagination from transactions
@st.cache_data
def fetch_products(offset=0, limit=20):
    query = f"""
    SELECT 
        JSONExtractString(data, 'cod_transacao') AS cod_transacao,
        groupArray(JSONExtractString(data, 'cod_prod')) AS products_sold_together,
        SUM(CAST(JSONExtractFloat(data, 'preco') AS Float64) * CAST(JSONExtractFloat(data, 'quantidade') AS Float64)) AS total_sales_value
    FROM grupox
    WHERE tag = 'transactions'
    GROUP BY cod_transacao
    HAVING COUNT(DISTINCT JSONExtractString(data, 'cod_prod')) > 1
    ORDER BY cod_transacao
    LIMIT {limit} OFFSET {offset}
    """
    return query_clickhouse(query)

# Function to extract distinct products from transactions
def get_all_products(products_data, product_details):
    all_products = set()
    for entry in products_data:
        products = entry[1]  # products_sold_together is at index 1
        all_products.update(products)
    
    # Map cod_prod to product names
    return [product_details.get(prod, {"cod_prod": prod, "nome_abrev": f"Produto: {prod}"}) for prod in all_products]

# Function to find related products for a selected product
def get_related_products(products_data, selected_product):
    for entry in products_data:
        products_sold_together = entry[1]  # products_sold_together is at index 1
        if selected_product['cod_prod'] in products_sold_together:
            related_products = products_sold_together.copy()
            related_products.remove(selected_product['cod_prod'])  # Exclude the selected product
            return related_products
    return []

# Main function to display the product catalog with search and pagination
def product_catalog():
    if 'authentication_status' not in st.session_state or st.session_state["authentication_status"] == False:
        st.switch_page('pages/login.py')
    else:
        st.title("Catálogo de Produtos")

        # Fetch product details from sku_dataset
        product_details_data = fetch_product_details()

        # Convert to a dictionary with cod_prod as keys
        product_details = {entry[0]: {"cod_prod": entry[0], "nome_abrev": entry[1], "nome_completo": entry[2]} for entry in product_details_data}

        # Pagination parameters
        items_per_page = 10
        current_page = st.session_state.get('current_page', 0)

        # Fetch products for the current page
        offset = current_page * items_per_page
        products_data = fetch_products(offset=offset, limit=items_per_page)

        if not products_data:
            st.write("No products found.")
            return
        
        # Extract all distinct products for this page
        all_products = get_all_products(products_data, product_details)

        # --- Search Bar ---
        search_query = st.text_input("Search by product name or ID", value="")

        # Filter products based on the search query (if any)
        if search_query:
            all_products = [
                prod for prod in all_products 
                if search_query.lower() in prod['nome_abrev'].lower() or search_query in prod['cod_prod']
            ]

        # Display products in a grid
        if all_products:
            cols = []
            num_cols = math.ceil(len(all_products) / 3)

            for i in range(0, num_cols):
                col = st.columns(3)
                cols.extend(col)

            count = 0

            # Displaying products with pagination
            for product in all_products:
                with cols[count]:
                    st.markdown(f'<div class="card"><h1>{product["nome_abrev"]}</h1></div>', unsafe_allow_html=True)
                    if st.button('Mais detalhes', key=product['cod_prod']):
                        product_details_page(product, products_data, product_details)
                count += 1
        else:
            st.write("No products match your search.")

        # Pagination controls
        col1, col2, col3 = st.columns([1, 1, 1])
        if col1.button("Previous") and current_page > 0:
            st.session_state['current_page'] = current_page - 1
            st.experimental_rerun()

        col2.write(f"Page {current_page + 1}")

        if col3.button("Next") and len(all_products) == items_per_page:
            st.session_state['current_page'] = current_page + 1
            st.experimental_rerun()

# Function to display product details and related products
def product_details_page(selected_product, products_data, product_details):
    # Display full product name in details
    st.markdown(f'<div class="card"><h2>{selected_product["nome_completo"]}</h2></div>', unsafe_allow_html=True)
    st.write(f"ID do Produto: {selected_product['cod_prod']}")

    # Find related products
    related_products = get_related_products(products_data, selected_product)

    if related_products:
        st.title('Produtos Relacionados')

        for related_product in related_products:
            related_prod_details = product_details.get(related_product, {"nome_abrev": f"Produto: {related_product}"})
            with st.expander(f"Produto Relacionado: {related_prod_details['nome_abrev']}"):
                st.write(f"ID: {related_product}")
    else:
        st.write("Nenhum produto relacionado encontrado.")

# Run the product catalog
product_catalog()
