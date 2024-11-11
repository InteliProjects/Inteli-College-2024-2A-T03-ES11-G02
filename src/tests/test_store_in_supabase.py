# import pytest
# import pandas as pd
# from unittest.mock import patch, MagicMock
# import os
# import sys

# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
# from src.utils.supabase_utils import store_in_supabase

# @patch.dict(os.environ, {
#     "SUPABASE_DB": "mock_db",
#     "SUPABASE_USER": "mock_user",
#     "SUPABASE_PASSWORD": "mock_password",
#     "SUPABASE_HOST": "mock_host",
#     "SUPABASE_PORT": "5432",
#     "CLICKHOUSE_HOST": "mock_clickhouse_host"  # Add this line to set CLICKHOUSE_HOST
# })
# @patch("psycopg2.connect")
# @patch("psycopg2.extras.execute_values")
# def test_store_in_supabase(mock_execute_values, mock_connect, tmp_path):
#     # Mock the connection and cursor
#     mock_conn = MagicMock()
#     mock_cursor = MagicMock()
#     mock_connect.return_value = mock_conn
#     mock_conn.cursor.return_value = mock_cursor

#     # Create a DataFrame to store
#     df = pd.DataFrame({
#         'col1': [1, 2],
#         'col2': ['A', 'B']
#     })

#     # Call the function
#     store_in_supabase(df, "test_table")

#     # Verify that the SQL command was executed
#     mock_execute_values.assert_called_once_with(
#         mock_cursor,
#         "INSERT INTO private_schema.test_table (col1, col2) VALUES %s",
#         [[1, 'A'], [2, 'B']],  # Adjusted to match the actual list of lists
#         template=None,
#         page_size=10000
#     )
#     mock_conn.commit.assert_called_once()
#     mock_conn.close.assert_called_once()
