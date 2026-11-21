FROM apache/airflow:2.5.1

USER airflow

RUN pip install --no-cache-dir \
    "apache-airflow==2.5.1" \
    "apache-airflow-providers-databricks==4.2.0"