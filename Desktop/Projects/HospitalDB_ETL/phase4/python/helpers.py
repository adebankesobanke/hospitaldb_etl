import pandas as pd
from sqlalchemy import create_engine

def create_db_engine(db_config):
    """Return SQLAlchemy engine."""
    url = f"postgresql+psycopg2://{db_config['user']}:{db_config['password']}@{db_config['host']}:{db_config['port']}/{db_config['database']}"
    return create_engine(url)

def load_csv_to_table(csv_path, table_name, engine):
    df = pd.read_csv(csv_path)
    df.to_sql(table_name, engine, if_exists='replace', index=False)
    print(f"[INFO] Loaded {len(df)} rows into {table_name}")
