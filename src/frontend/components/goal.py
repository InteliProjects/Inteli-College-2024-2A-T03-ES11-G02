import streamlit as st

def goal(label, target, total, due_date):
    st.metric(label=label, value=f"{target} / {total}", delta=f"{((target * 100) / total):.1f}%")
    st.progress(target / total)
    st.write(f'Até {due_date}')
