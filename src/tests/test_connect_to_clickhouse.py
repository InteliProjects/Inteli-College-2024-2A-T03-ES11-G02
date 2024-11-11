import pytest
from unittest.mock import patch, MagicMock
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

# Patch environment variables before importing the module
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
@patch('clickhouse_connect.get_client')
def test_connect_to_clickhouse(mock_get_client):
    from src.utils.connections import connect_to_clickhouse  # Import inside the test after patching
    mock_client = mock_get_client.return_value
    client = connect_to_clickhouse()
    mock_get_client.assert_called_once()
    assert client == mock_client, "Deveria retornar o cliente mockado"
