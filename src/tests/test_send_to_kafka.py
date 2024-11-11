# import pytest
# import pandas as pd
# from unittest.mock import patch, MagicMock, call
# import os
# import sys

# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
# from src.src.ingestion.data_ingestion_pipeline import send_to_kafka

# @patch.dict(os.environ, {
#     "KAFKA_BOOTSTRAP_SERVERS": "localhost:9092"
# })
# @patch("kafka.KafkaProducer")
# def test_send_to_kafka(mock_kafka_producer_class):
#     # Mock KafkaProducer instance
#     mock_kafka_producer_instance = mock_kafka_producer_class.return_value
    
#     # Debugging statement to verify mock setup
#     print(f"KafkaProducer instance: {mock_kafka_producer_instance}")
    
#     # Create a test DataFrame
#     df = pd.DataFrame({
#         'col1': [1, 2],
#         'col2': ['A', 'B']
#     })
    
#     # Call the function
#     send_to_kafka("test_topic", df, "test_table")
    
#     # Ensure the send method was called twice (once for each row)
#     assert mock_kafka_producer_instance.send.call_count == 2, f"Expected 2 calls to KafkaProducer's send method, but got {mock_kafka_producer_instance.send.call_count}"
    
#     # Check that each call to send had the correct data
#     expected_calls = [
#         call("test_topic", value={"table_name": "test_table", "data": {"col1": 1, "col2": "A"}}),
#         call("test_topic", value={"table_name": "test_table", "data": {"col1": 2, "col2": "B"}})
#     ]
#     mock_kafka_producer_instance.send.assert_has_calls(expected_calls, any_order=True)
    
#     # Ensure flush was called
#     mock_kafka_producer_instance.flush.assert_called_once()
