# import os
# import json
# import logging
# import pandas as pd
# import clickhouse_connect
# import pika  # RabbitMQ library for Python
# from tqdm import tqdm
# from dotenv import load_dotenv

# # Load environment variables
# load_dotenv()

# # RabbitMQ connection settings
# RABBITMQ_HOST = os.getenv('RABBITMQ_HOST', 'localhost')

# # ClickHouse credentials from .env file
# CLICKHOUSE_HOST = os.getenv("CLICKHOUSE_HOST").strip()
# CLICKHOUSE_PORT = os.getenv("CLICKHOUSE_PORT").strip()
# CLICKHOUSE_USER = os.getenv("CLICKHOUSE_USER").strip()
# CLICKHOUSE_PASSWORD = os.getenv("CLICKHOUSE_PASSWORD").strip()
# CLICKHOUSE_DB = os.getenv("CLICKHOUSE_DB", "default").strip()

# BATCH_SIZE = 15000  # Batch size for preloading data

# # Logging configuration
# logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


# # Function to connect to ClickHouse
# def connect_to_clickhouse():
#     logging.info("Connecting to ClickHouse...")
#     client = clickhouse_connect.get_client(
#         host=CLICKHOUSE_HOST,
#         port=CLICKHOUSE_PORT,
#         username=CLICKHOUSE_USER,
#         password=CLICKHOUSE_PASSWORD,
#         database=CLICKHOUSE_DB,
#         secure=True,
#         verify=False
#     )
#     logging.info("Connected to ClickHouse.")
#     return client


# # Function to connect to RabbitMQ
# def connect_to_rabbitmq():
#     logging.info("Connecting to RabbitMQ...")
#     connection = pika.BlockingConnection(pika.ConnectionParameters(host=RABBITMQ_HOST))
#     channel = connection.channel()
#     channel.queue_declare(queue='data_queue', durable=True)
#     logging.info("Connected to RabbitMQ.")
#     return connection, channel


# # Function to preprocess data (cleaning, normalizing, etc.)
# def preprocess_data(df):
#     logging.info("Starting data preprocessing...")

#     # Clean data (removing nulls)
#     df.dropna(inplace=True)

#     # Normalize data (lowercase for strings)
#     df = df.applymap(lambda x: x.lower() if isinstance(x, str) else x)

#     # Convert datetime fields to strings
#     for col in df.select_dtypes(include=['datetime']):
#         df[col] = df[col].dt.strftime('%Y-%m-%d %H:%M:%S')

#     logging.info("Data preprocessing completed.")
#     return df


# # Function to preload and send data to RabbitMQ in batches
# def preload_data(client, channel):
#     logging.info(f"Starting data preloading with batch size {BATCH_SIZE}...")

#     # Query the number of rows in the original table
#     count_query = "SELECT count(*) FROM grupox"
#     total_rows = client.command(count_query)

#     logging.info(f"Total rows to process: {total_rows}")

#     # Process the data in batches
#     for offset in tqdm(range(0, total_rows, BATCH_SIZE)):
#         batch_query = f"SELECT data, date_time, tag FROM grupox LIMIT {BATCH_SIZE} OFFSET {offset}"
#         result = client.query(batch_query)
#         rows = result.result_rows

#         # Convert the result into a Pandas DataFrame
#         df = pd.DataFrame(rows, columns=["data", "date_time", "tag"])

#         # Preprocess the data
#         df = preprocess_data(df)

#         # Convert DataFrame to a list of JSON messages
#         messages = df.to_dict(orient="records")

#         # Send the entire batch as a single RabbitMQ message
#         channel.basic_publish(
#             exchange='',
#             routing_key='data_queue',
#             body=json.dumps(messages),  # Sending the entire batch as JSON
#             properties=pika.BasicProperties(
#                 delivery_mode=2,  # Make the message persistent
#             )
#         )

#         logging.info(f"Sent {len(df)} rows to RabbitMQ.")

#     logging.info("Data preloading completed.")


# if __name__ == "__main__":
#     client = connect_to_clickhouse()
#     connection, channel = connect_to_rabbitmq()
#     try:
#         preload_data(client, channel)
#     finally:
#         connection.close()
