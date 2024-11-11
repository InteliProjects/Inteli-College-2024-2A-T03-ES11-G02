import streamlit as st
import streamlit_authenticator as stauth
import os

# Get the absolute path of the current file (main.py)
current_dir = os.path.dirname(os.path.abspath(__file__))

# Use the absolute path to reference style.css
style_path = os.path.join(current_dir, 'style.css')

# Safely open and read style.css if it exists
if os.path.exists(style_path):
    with open(style_path) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
else:
    st.error("style.css file not found")

# Your existing logic for navigation and authentication
pages = {
    "DataApp" : [
        st.Page(
            'pages/dashboard.py',
            title="DASHBOARD"
        ),
        st.Page(
            'pages/products.py',
            title="PRODUTOS"
        ),
        st.Page(
            'pages/transactions.py',
            title="TRANSAÇÕES"
        ),
        st.Page(
            'pages/add_data.py',
            title="ADD-DATA"
        ),
        st.Page(
            'pages/data_builder.py',
            title="DATA-BUILDER"
        ),
    ]
}

pg = st.navigation(pages, position="sidebar")

data = {
    'usernames': {
        'alice_s': {
            'id': 12340,
            'email': 'alice_s@gmail.com',
            'name': 'Alice',
            'password': '123',
            'role': 'admin',
            'store': 'Loja A'
        },
        'bob_a': {
            'id': 12341,
            'email': 'bob_a@gmail.com',
            'name': 'Bob',
            'password': '456',
            'role': 'manager',
            'store': 'Loja A'
        },
        'charlie_d': {
            'id': 12342,
            'email': 'charlie_d@gmail.com',
            'name': 'Charlie',
            'password': '789',
            'role': 'vendor',
            'store': 'Loja A'
        }
    }
}

passwords = [data['usernames'][username]['password'] for username in data['usernames']]

hashed_passwords = stauth.Hasher(passwords).generate()
for i, username in enumerate(data['usernames']):
    data['usernames'][username]['password'] = hashed_passwords[i]

authenticator = stauth.Authenticate(
    credentials=data,
    cookie_name='streamlit-authenticator-example',
    cookie_key='streamlit-authenticator-signing-key',
    cookie_expiry_days=1
)

name, authenticator_status, username = authenticator.login('main')

if st.session_state["authentication_status"] == False:
    st.write('Usuário ou senha incorretos')

elif st.session_state["authentication_status"]:
    authenticator.logout('Logout', 'sidebar')
    st.write(f'Bem vindo **{st.session_state["name"]}**')
    st.session_state['role'] = data['usernames'][username]['role']
    st.session_state['store'] = data['usernames'][username]['store']
    st.session_state['id'] = data['usernames'][username]['id']
    pg.run()
