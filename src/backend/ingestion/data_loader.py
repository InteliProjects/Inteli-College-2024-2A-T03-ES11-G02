import pandas as pd
import logging
import sys
import os

# Add the top-level 'src' directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

# Now you can import your modules from utils
from backend.utils.retry import retry_on_failure


@retry_on_failure
def load_data(file_path, expected_columns, delimiter=","):
    """Carrega o arquivo CSV e verifica se as colunas são as esperadas."""
    df = pd.read_csv(file_path, encoding="ISO-8859-1", delimiter=delimiter, on_bad_lines='skip')
    if len(df.columns) != len(expected_columns):
        logging.warning(f"O arquivo {file_path} tem um número inesperado de colunas.")
        logging.warning(f"Esperado: {expected_columns}")
        logging.warning(f"Encontrado: {df.columns.tolist()}")
        df = df.dropna(how="all", axis=1)
        if len(df.columns) != len(expected_columns):
            raise ValueError(f"Não foi possível corrigir as colunas no arquivo {file_path}. Verifique manualmente.")
        df.columns = expected_columns
    return df
