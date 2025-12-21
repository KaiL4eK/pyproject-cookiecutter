import time

from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator
from airflow.providers.postgres.hooks.postgres import PostgresHook
from pendulum import datetime

from {{cookiecutter.project_slug}}.airflow.sensors.async_pg_sql_sensor import (
    DeferrableAsyncSqlSensor,
)


def sleep_task():
    time.sleep(1)


def delete_sample_row():
    hook = PostgresHook(postgres_conn_id="sample_postgres_connection")
    hook.run(
        "DELETE FROM wait_table WHERE data = %s;",
        parameters=("sample data",),
    )


with DAG(
    dag_id="wait_and_delete_row",
    start_date=datetime(2025, 4, 25),
    catchup=False,
    tags=["example", "deferrable", "postgres"],
) as dag:
    wait_for_row = DeferrableAsyncSqlSensor(
        task_id="wait_for_row",
        conn_id="sample_postgres_connection",
        sql="SELECT id FROM wait_table WHERE data = 'sample data';",
        poke_interval=15,
        timeout=300,
    )

    sleep = PythonOperator(
        task_id="sleep_task",
        python_callable=sleep_task,
    )

    delete_row = PythonOperator(
        task_id="delete_sample_row",
        python_callable=delete_sample_row,
    )

    sleep >> wait_for_row >> delete_row
