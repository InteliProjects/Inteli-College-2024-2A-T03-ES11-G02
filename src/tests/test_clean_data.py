import pytest
import pandas as pd
from unittest.mock import patch
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

@patch.dict(os.environ, {
    "CLICKHOUSE_HOST": "mock_host",
    "CLICKHOUSE_PORT": "9000",
    "CLICKHOUSE_USER": "mock_user",
    "CLICKHOUSE_PASSWORD": "mock_password",
    "CLICKHOUSE_DB": "default",
    "SUPABASE_DB": "mock_db",
    "SUPABASE_USER": "mock_user",
    "SUPABASE_PASSWORD": "mock_password",
    "SUPABASE_HOST": "mock_host",
    "SUPABASE_PORT": "5432"
})
def test_clean_data():
    from src.backend.processing.data_cleaning import clean_data  # Import inside the test after patching

    df = pd.DataFrame({
        'col1': [1, 2, None],
        'col2': ['a', None, 'b']
    })
    cleaned_df = clean_data(df)
    assert cleaned_df.isnull().sum().sum() == 0, "Não deveria haver valores nulos após a limpeza"
    assert len(cleaned_df) == 1, "O DataFrame deve conter apenas linhas válidas"
