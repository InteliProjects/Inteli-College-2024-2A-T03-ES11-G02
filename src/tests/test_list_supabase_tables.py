import pytest
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
def test_list_supabase_tables(mock_connect):
    from src.backend.processing.data_extraction import list_supabase_tables  # Import inside the test after patching
    mock_conn = mock_connect.return_value
    mock_cursor = mock_conn.cursor.return_value
    mock_cursor.fetchall.return_value = [('table1',), ('table2',)]
    
    tables = list_supabase_tables(mock_conn)
    mock_conn.cursor.assert_called_once()
    mock_cursor.execute.assert_called_once()
    assert tables == ['table1', 'table2'], "Deveria retornar a lista de tabelas mockadas"
