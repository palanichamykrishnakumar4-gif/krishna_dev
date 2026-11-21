from datetime import datetime, timedelta

from airflow import DAG

from airflow.providers.databricks.operators.databricks import (
    DatabricksRunNowOperator
)

default_args = {
    "owner": "krishna",
    "depends_on_past": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=2)
}

with DAG(
    dag_id="databricks_sales_demo",
    default_args=default_args,
    description="Airflow triggers Databricks PySpark job",
    start_date=datetime(2026, 11, 21),
    schedule_interval=None,
    catchup=False,
    tags=["databricks", "pyspark", "demo"]
) as dag:

    run_sales_notebook = DatabricksRunNowOperator(
        task_id="run_sales_notebook",
        databricks_conn_id="databricks_default",
        job_id=70340221391152,
        polling_period_seconds=15,
        wait_for_termination=True
    )

    run_sales_notebook