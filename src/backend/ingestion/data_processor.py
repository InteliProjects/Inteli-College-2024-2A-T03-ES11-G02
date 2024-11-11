import pandas as pd
import sys
import os

# Add the top-level 'src' directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

# Now you can import your modules from utils
from backend.utils.retry import retry_on_failure


@retry_on_failure
def process_data(df, date_columns):
    """Converte colunas de data para o formato adequado."""
    for col in date_columns:
        df[col] = pd.to_datetime(df[col], errors='coerce', dayfirst=True)
        df[col] = df[col].apply(lambda x: x.strftime('%Y-%m-%d %H:%M:%S') if pd.notnull(x) else None)
    return df
