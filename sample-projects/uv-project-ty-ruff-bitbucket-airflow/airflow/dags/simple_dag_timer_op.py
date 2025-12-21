"""Sample DAG with time operator."""

from datetime import datetime, timedelta, timezone

from airflow.sdk import dag
from airflow.providers.standard.sensors.time import TimeSensorAsync

from uv_project_ty_ruff_bitbucket_airflow.airflow.tasks import (
    sample_sleep_task,
    show_logic_time_task,
    show_sample_variable,
    simple_task_operator,
    simple_task_taskflow,
)


@dag(
    dag_id="simple-dag-timer-op",
    start_date=datetime(2025, 1, 1),  # noqa: DTZ001
    catchup=False,
)
def simple_dag() -> None:
    """Sample DAG with time operator."""
    sample_async_timer_sensor = TimeSensorAsync(
        task_id="timeout_after_second_date_in_the_future",
        timeout=10,
        soft_fail=True,
        target_time=(datetime.now(tz=timezone.utc) + timedelta(minutes=1)).time(),
    )

    (
        simple_task_taskflow()
        >> simple_task_operator
        >> sample_sleep_task(sleep_time=10)
        >> sample_sleep_task(sleep_time=4)
        >> sample_async_timer_sensor
        >> show_logic_time_task()
        >> show_sample_variable()
    )


simple_dag()
