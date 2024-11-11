import pytest
import pandas as pd
from unittest.mock import patch
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from src.backend.ingestion.data_processor import process_data

def test_process_data():
    df = pd.DataFrame({
        'date_column': ["01/01/2023", "31/12/2022", None]
    })
    date_columns = ["date_column"]
    processed_df = process_data(df, date_columns)

    assert processed_df['date_column'].iloc[0] == "2023-01-01 00:00:00"
    assert processed_df['date_column'].iloc[1] == "2022-12-31 00:00:00"
    assert processed_df['date_column'].iloc[2] is None, "None values should remain None"
