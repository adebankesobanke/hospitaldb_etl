from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from phase4.python.etl_pipeline import run_etl

default_args = {
    "owner": "you",
    "start_date": datetime(2025, 12, 10),
    "retries": 1,
}

with DAG(
    dag_id="hospitaldb_etl",
    default_args=default_args,
    schedule_interval="@daily",
    catchup=False,
) as dag:

    run_etl_task = PythonOperator(
        task_id="run_etl",
        python_callable=run_etl
    )

    run_etl_task
