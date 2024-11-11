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
@patch('clickhouse_connect.get_client')
def test_load_data_to_clickhouse(mock_get_client):
    from backend.utils.clickhouse_utils import load_data_to_clickhouse  # Import inside the test after patching
    mock_client = mock_get_client.return_value
    df = pd.DataFrame({
        'data': ['{"amount": 100}', '{"amount": 200}'],
        'date_time': ['2023-01-01 00:00:00', '2023-01-02 00:00:00'],
        'tag': ['test_table', 'test_table']
    })
    load_data_to_clickhouse(mock_client, df)
    mock_client.command.assert_called_once()
