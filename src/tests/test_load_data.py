# import pytest
# import pandas as pd
# from unittest.mock import patch, MagicMock
# import os
# import sys

# # Mock KafkaProducer and KafkaConsumer to prevent them from causing import issues
# sys.modules['kafka'] = MagicMock()
# sys.modules['kafka.KafkaProducer'] = MagicMock()
# sys.modules['kafka.KafkaConsumer'] = MagicMock()

# # Append the correct path to load the module
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

# from src.backend.ingestion.ingestion import load_data


# @patch.dict(os.environ, {
#     "SUPABASE_DB": "mock_db",
#     "SUPABASE_USER": "mock_user",
#     "SUPABASE_PASSWORD": "mock_password",
#     "SUPABASE_HOST": "mock_host",
#     "SUPABASE_PORT": "5432"
# })
# def test_load_data(tmp_path):
#     csv_content = "col1,col2\n1,2\n3,4"
#     file_path = tmp_path / "test.csv"
#     with open(file_path, 'w') as f:
#         f.write(csv_content)

#     expected_columns = ["col1", "col2"]
#     df = load_data(file_path, expected_columns)

#     assert list(df.columns) == expected_columns, "Loaded DataFrame should have the expected columns"
#     assert df.shape == (2, 2), "Loaded DataFrame should have 2 rows and 2 columns"
