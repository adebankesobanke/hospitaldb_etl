
Full ETL Pipeline for HospitalDB Phase 4
"""

from helpers import (
    create_db_engine,
    load_csv_to_table,
    run_sql_file,
    run_data_quality_check
)
from config import CSV_PATHS

def extract(engine):
    """Load raw CSVs into raw tables."""
    load_csv_to_table(CSV_PATHS["patients"], "raw_patients", engine)
    load_csv_to_table(CSV_PATHS["visits"], "raw_visits", engine)
    load_csv_to_table(CSV_PATHS["billing"], "raw_billing", engine)


def transform(engine):
    """Execute SQL transformations to populate staging tables."""
    run_sql_file(engine, "phase1/sql/staging_tables/stg_patients.sql")
    run_sql_file(engine, "phase1/sql/staging_tables/stg_visits.sql")
    run_sql_file(engine, "phase1/sql/staging_tables/stg_billing.sql")


def load_dimension_and_fact(engine):
    """Load dimension and fact tables from Phase 3."""
    run_sql_file(engine, "phase3/sql/dimension_tables/dim_patient.sql")
    run_sql_file(engine, "phase3/sql/dimension_tables/dim_doctor.sql")
    run_sql_file(engine, "phase3/sql/dimension_tables/dim_department.sql")
    run_sql_file(engine, "phase3/sql/dimension_tables/dim_time.sql")

    run_sql_file(engine, "phase3/sql/fact_tables/fact_visits.sql")
    run_sql_file(engine, "phase3/sql/fact_tables/fact_billing.sql")
    run_sql_file(engine, "phase3/sql/fact_tables/fact_lab_results.sql")
    run_sql_file(engine, "phase3/sql/fact_tables/fact_medications.sql")


def run_dq_checks(engine):
    """Perform crucial DQ validations."""

    # Check for NULL patient IDs
    run_data_quality_check(
        engine,
        "Null patient_id in visits",
        """
        SELECT * FROM stg_visits
        WHERE patient_id IS NULL;
        """
    )

    # Check for unknown billing statuses
    run_data_quality_check(
        engine,
        "Invalid billing status",
        """
        SELECT * FROM stg_billing
        WHERE status NOT IN ('PAID', 'PENDING', 'DENIED');
        """
    )


def main():
    engine = create_db_engine()

    print("RUNNING EXTRACTION...")
    extract(engine)

    print("RUNNING TRANSFORMATION...")
    transform(engine)

    print("RUNNING DQ CHECKS...")
    run_dq_checks(engine)

    print("LOADING DIMENSIONS & FACTS...")
    load_dimension_and_fact(engine)

    print("ETL COMPLETED SUCCESSFULLY.")


if __name__ == "__main__":
    main()

