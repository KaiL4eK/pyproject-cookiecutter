"""Sample DAG."""

import random
import string
from datetime import datetime

from airflow.sdk import dag, task
from airflow.operators.trigger_dagrun import TriggerDagRunOperator

from uv_project_ty_ruff_bitbucket_airflow.airflow.tasks import (
    show_sample_variable,
    simple_task_taskflow,
)

# 3 MiB in bytes
PAYLOAD_SIZE = int(0.5 * 1024 * 1024)
CHARS = string.ascii_letters + string.digits

# Build 500 conf dicts, each with a ~3 MiB random string


@task
def create_random_strings() -> list[str]:
    return ["".join(random.choices(CHARS, k=PAYLOAD_SIZE)) for i in range(500)]


@dag(
    dag_id="expand-dags-trigger",
    start_date=datetime(2025, 1, 1),  # noqa: DTZ001
    catchup=False,
)
def simple_dag() -> None:
    payloads = create_random_strings()

    trigger_source_files_parsing = TriggerDagRunOperator.partial(
        task_id="trigger_source_parsing",
        task_display_name="Source files parsing",
        trigger_dag_id="simple-dag",
        wait_for_completion=True,
        deferrable=True,
        poke_interval=10,
    ).expand_kwargs(
        payloads.map(
            lambda data: {
                "conf": {
                    "matched_source_metrics": data,
                    "source_file_location": "dummy",
                }
            }
        )
    )

    (
        simple_task_taskflow()
        >> trigger_source_files_parsing
        >> show_sample_variable()
    )


simple_dag()
