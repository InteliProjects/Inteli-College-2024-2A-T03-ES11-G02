import streamlit as st
import os
import subprocess

st.title("Add Data")

uploaded_file = st.file_uploader("Upload a CSV file", type="csv")

if uploaded_file is not None:
    # Save the file temporarily to raw data folder
    raw_data_path = os.path.join("src/data/raw", uploaded_file.name)
    with open(raw_data_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    st.success(f"File saved to {raw_data_path}")

    # Trigger data ingestion and processing scripts
    if st.button("Start Ingestion and Processing"):
        st.write("Running ingestion pipeline...")
        subprocess.run(["python", "src/src/ingestion/data_ingestion_pipeline.py"])
        st.write("Running processing script...")
        subprocess.run(["python", "src/src/processing/processing_And_Storage.py"])
        st.success("Data ingestion and processing completed.")
