# airflow/sensors/async_sql_sensor.py

from airflow.hooks.base import BaseHook
from airflow.sensors.base import BaseSensorOperator
from airflow.triggers.base import TriggerEvent

from ..triggers.async_pg_sql_trigger import AsyncPgSqlTrigger


class DeferrableAsyncSqlSensor(BaseSensorOperator):
    """
    Deferrable-сенсор для PostgreSQL, который уходит в ожидание к AsyncPgSqlTrigger.
    """

    template_fields = ("sql",)
    template_ext = (".sql",)

    def __init__(
        self,
        *,
        conn_id: str,
        sql: str,
        poke_interval: float = 60,
        **kwargs,
    ) -> None:
        super().__init__(**kwargs)
        # Синхронно забираем параметры подключения из Airflow
        conn = BaseHook.get_connection(conn_id)
        self.conn_config = {
            "host": conn.host,
            "port": conn.port or 5432,
            "user": conn.login,
            "password": conn.password,
            "database": conn.schema,
        }
        self.sql = sql
        self.poke_interval = poke_interval

    def execute(self, context):
        # Уходим в deferred режим, передаём наш AsyncPgSqlTrigger
        self.defer(
            trigger=AsyncPgSqlTrigger(
                conn_config=self.conn_config,
                sql=self.sql,
                poke_interval=self.poke_interval,
            ),
            method_name="execute_complete",
        )

    def execute_complete(self, context, event: TriggerEvent = None):
        # При завершении возвращаем данные (или None)
        return event
