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
def test_connect_to_supabase(mock_connect):
    from backend.utils.connections import connect_to_supabase  # Import inside the test after patching
    mock_conn = mock_connect.return_value
    conn = connect_to_supabase()
    mock_connect.assert_called_once()
    assert conn == mock_conn, "Deveria retornar a conexão mockada"
