import os
from dotenv import load_dotenv

# Carrega as variáveis do arquivo .env
load_dotenv()

# Função para garantir que a variável de ambiente está definida e não é None
def get_env_variable(var_name, default_value=None):
    value = os.getenv(var_name, default_value)
    if value is None:
        raise ValueError(f"Environment variable {var_name} is not set.")
    return value.strip()

# Configurações do Supabase
SUPABASE_DB = get_env_variable("SUPABASE_DB")
SUPABASE_USER = get_env_variable("SUPABASE_USER")
SUPABASE_PASSWORD = get_env_variable("SUPABASE_PASSWORD")
SUPABASE_HOST = get_env_variable("SUPABASE_HOST")
SUPABASE_PORT = get_env_variable("SUPABASE_PORT", "5432")  # Valor padrão 5432

# Configurações do ClickHouse
CLICKHOUSE_HOST = get_env_variable("CLICKHOUSE_HOST")
CLICKHOUSE_PORT = get_env_variable("CLICKHOUSE_PORT")
CLICKHOUSE_USER = get_env_variable("CLICKHOUSE_USER")
CLICKHOUSE_PASSWORD = get_env_variable("CLICKHOUSE_PASSWORD")
CLICKHOUSE_DB = get_env_variable("CLICKHOUSE_DB", "default")

# Outras configurações
TIMEOUT = 60000000000  # ou um valor configurável, se necessário
BATCH_SIZE = int(get_env_variable("BATCH_SIZE", 15000))
KAFKA_BOOTSTRAP_SERVERS = get_env_variable("KAFKA_BOOTSTRAP_SERVERS", "localhost:9092")

# Definir o diretório de dados processados
PROCESSED_DATA_DIR = os.path.join(os.path.dirname(__file__), '../../data/processed')
os.makedirs(PROCESSED_DATA_DIR, exist_ok=True)

print("Configurações carregadas com sucesso.")
