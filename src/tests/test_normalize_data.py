import pytest
import pandas as pd
from unittest.mock import patch, MagicMock
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
def test_normalize_data():
    from src.backend.processing.data_cleaning import normalize_data  # Import inside the test after patching

    df = pd.DataFrame({
        'col1': ['A', 'B', 'C'],
        'date_time': pd.to_datetime(['2023-01-01', '2023-02-01', '2023-03-01'])
    })
    normalized_df = normalize_data(df)
    assert all(normalized_df['col1'] == ['a', 'b', 'c']), "Todos os valores de string devem estar em minúsculas"
    assert normalized_df['date_time'].dtype == 'object', "As datas devem ser strings formatadas"
