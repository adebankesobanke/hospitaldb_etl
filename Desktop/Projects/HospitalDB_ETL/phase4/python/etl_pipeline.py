"""
Simple ETL pipeline entrypoint for Phase 4.
"""

from config import DB_CONFIG, CSV_PATHS
from helpers import create_db_engine, load_csv_to_table

def run_etl():
    engine = create_db_engine(DB_CONFIG)
    # Load CSVs into raw tables (example)
    load_csv_to_table(CSV_PATHS['patients'], 'raw_patients', engine)
    load_csv_to_table(CSV_PATHS['visits'], 'raw_visits', engine)
    load_csv_to_table(CSV_PATHS['billing'], 'raw_billing', engine)
    # TODO: add transforms -> staging, DQ checks, loads to dim/fact
    print("ETL run completed.")

if __name__ == "__main__":
    run_etl()
