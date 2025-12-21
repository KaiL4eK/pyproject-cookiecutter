from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator
from airflow.providers.postgres.hooks.postgres import PostgresHook
from pendulum import datetime


def create_wait_table():
    hook = PostgresHook(postgres_conn_id="sample_postgres_connection")
    hook.run(
        """
        CREATE TABLE IF NOT EXISTS wait_table (
            id SERIAL PRIMARY KEY,
            data TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT now()
        );
        """,
    )

def create_result_table():
    hook = PostgresHook(postgres_conn_id="sample_postgres_connection")
    hook.run(
        """
        CREATE TABLE IF NOT EXISTS result_table (
            id SERIAL PRIMARY KEY,
            task_index INT NOT NULL,
            execution_time TIMESTAMP DEFAULT now()
        );
        """,
    )

def insert_sample_row():
    hook = PostgresHook(postgres_conn_id="sample_postgres_connection")
    hook.run(
        "INSERT INTO wait_table (data) VALUES (%s);",
        parameters=("sample data",),
    )

with DAG(
    dag_id="create_and_insert_row",
    start_date=datetime(2025, 4, 25),
    schedule=None,
    catchup=False,
    max_active_runs=1,
    tags=["postgres"],
) as dag:

    create_table = PythonOperator(
        task_id="create_wait_table",
        python_callable=create_wait_table,
    )

    create_table_2 = PythonOperator(
        task_id="create_result_table",
        python_callable=create_result_table,
    )

    insert_row = PythonOperator(
        task_id="insert_sample_row",
        python_callable=insert_sample_row,
    )

    create_table >> create_table_2 >> insert_row
