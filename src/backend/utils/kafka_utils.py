import json
from kafka import KafkaProducer, KafkaConsumer
from tqdm import tqdm
import sys
import os
import logging
import pandas as pd
from backend.utils.supabase_utils import store_in_supabase
from backend.config.config import KAFKA_BOOTSTRAP_SERVERS
from backend.utils.retry import retry_on_failure

# Testa a conexão com o Kafka
def test_kafka_connection():
    """Test the connection to Kafka."""
    try:
        KafkaProducer(bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS)
        logging.info("Successfully connected to Kafka.")
    except Exception as e:
        logging.error(f"Failed to connect to Kafka: {e}")
        raise

@retry_on_failure
def send_to_kafka(topic, df, table_name):
    """Envia dados para o Kafka."""
    producer = KafkaProducer(bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
                             value_serializer=lambda v: json.dumps(v, default=str).encode('utf-8'))
    chunks = df.to_dict(orient='records')
    for chunk in tqdm(chunks, desc=f"Enviando {table_name} para o Kafka"):
        producer.send(topic, value={"table_name": table_name, "data": chunk})
    producer.flush()

@retry_on_failure
def kafka_to_supabase(topic):
    """Consome dados do Kafka e armazena no Supabase."""
    consumer = KafkaConsumer(topic,
                             bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
                             auto_offset_reset='earliest',
                             value_deserializer=lambda x: json.loads(x.decode('utf-8')))
    for message in consumer:
        table_name = message.value['table_name']
        data = message.value['data']
        df = pd.DataFrame([data])
        store_in_supabase(df, table_name)
