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
@patch('psycopg2.connect')
def test_extract_data_from_supabase(mock_connect):
    from src.backend.processing.data_extraction import extract_data_from_supabase  # Import inside the test after patching
    mock_conn = mock_connect.return_value
    mock_cursor = mock_conn.cursor.return_value
    mock_cursor.description = [('col1',), ('col2',)]
    mock_cursor.fetchmany.side_effect = [
        [('val1', 'val2')],
        []
    ]
    
    generator = extract_data_from_supabase(mock_conn, 'test_table')
    df = next(generator)
    
    assert isinstance(df, pd.DataFrame), "O resultado deve ser um DataFrame"
    assert df.columns.tolist() == ['col1', 'col2'], "As colunas do DataFrame devem corresponder à descrição mockada"
    assert not df.empty, "O DataFrame não deve estar vazio"
