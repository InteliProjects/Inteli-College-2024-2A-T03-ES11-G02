import pandas as pd
import sys
import os
import logging

# Add the top-level 'src' directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

# Import from the correct modules
from backend.utils.kafka_utils import send_to_kafka, kafka_to_supabase, test_kafka_connection
from backend.utils.supabase_utils import store_in_supabase, test_supabase_connection
from backend.ingestion.data_loader import load_data
from backend.ingestion.data_processor import process_data
from backend.config.config import PROCESSED_DATA_DIR

def main():
    """Função principal que executa o pipeline."""
    try:
        # Testa conexões
        logging.info("Testando conexão com o Supabase...")
        test_supabase_connection()
        
        logging.info("Testando conexão com o Kafka...")
        test_kafka_connection()

        # Conjunto de datasets
        datasets = {
            "employee_final": {
                "file": "../../data/raw/employee_final.csv",
                "expected_columns": ["id_employee", "name", "surname", "cpf", "status", "role", "initial_date", "end_date", "store_id"],
                "date_columns": ["initial_date", "end_date"]
            },
            "sku_cost": {
                "file": "../../data/raw/sku_cost.csv",
                "expected_columns": ["cod_prod", "data_inicio", "data_fim", "custo"],
                "date_columns": ["data_inicio", "data_fim"]
            },
            "sku_price": {
                "file": "../../data/raw/sku_price.csv",
                "expected_columns": ["cod_prod", "data_inicio", "data_fim", "preco"],
                "date_columns": ["data_inicio", "data_fim"]
            },
            "store_final": {
                "file": "../../data/raw/store_final.csv",
                "expected_columns": ["nome_loja", "regiao", "diretoria", "data_inauguracao"],
                "date_columns": ["data_inauguracao"]
            },
            "target_store_final": {
                "file": "../../data/raw/target_store_final.csv",
                "expected_columns": ["month", "store_id", "sales_target"],
                "date_columns": []
            },
            "targets_salesperson_final": {
                "file": "../../data/raw/targets_salesperson_final.csv",
                "expected_columns": ["id_employee", "sales_target", "month"],
                "date_columns": []
            },
            "sku_dataset": {
                "file": "../../data/raw/sku_dataset.csv",
                "expected_columns": ["cod_prod", "nome_abrev", "nome_completo", "descricao", "categoria", "sub_categoria", "marca", "conteudo_valor", "conteudo_medida"],
                "date_columns": [],
                "delimiter": ";"  
            },
            "sku_status_dataset": {
                "file": "../../data/raw/sku_status_dataset.csv",
                "expected_columns": ["cod_prod", "data_inicio", "data_fim"],
                "date_columns": ["data_inicio", "data_fim"],
                "delimiter": ";"  
            }
        }

        # Processa cada dataset
        for table_name, config in datasets.items():
            try:
                logging.info(f"Carregando e processando {table_name}...")
                df = load_data(config["file"], config["expected_columns"], delimiter=config.get("delimiter", ","))
                df = process_data(df, config["date_columns"])

                logging.info(f"Enviando {table_name} para o Kafka...")
                send_to_kafka("processed_data", df, table_name)

                logging.info(f"Armazenando {table_name} no Supabase...")
                store_in_supabase(df, table_name, batch_size=10000)

            except Exception as e:
                logging.error(f"Erro ao processar {table_name}: {e}")
                raise

        # Processamento de transações
        logging.info("Processando transações...")
        transaction_columns = ["data", "cod_vendedor", "cod_loja", "cod_transacao", "quantidade", "cod_prod", "preco"]
        transaction_files = [
            "../../data/raw/2018.csv",
            "../../data/raw/2019.csv",
            "../../data/raw/2020.csv",
            "../../data/raw/2021.csv",
            "../../data/raw/2022.csv",
            "../../data/raw/2023.csv",
            "../../data/raw/2024.csv"
        ]

        transaction_dfs = []
        for file in transaction_files:
            try:
                logging.info(f"Carregando {file}...")
                df = load_data(file, transaction_columns)
                transaction_dfs.append(df)
            except Exception as e:
                logging.error(f"Erro ao carregar arquivo de transação {file}: {e}")
                raise

        transactions_df = pd.concat(transaction_dfs, ignore_index=True)

        transactions_df = process_data(transactions_df, ["data"])
        transactions_df = transactions_df.sort_values(by="data")

        logging.info("Enviando transações para o Kafka...")
        send_to_kafka("processed_data", transactions_df, "transactions")

        logging.info("Armazenando transações no Supabase...")
        store_in_supabase(transactions_df, "transactions", batch_size=10000)

        # Consome dados do Kafka e armazena no Supabase
        logging.info("Consumindo dados do Kafka e armazenando no Supabase...")
        kafka_to_supabase("processed_data")

    except Exception as e:
        logging.error(f"Erro na execução do pipeline: {e}")
        raise

if __name__ == "__main__":
    main()
