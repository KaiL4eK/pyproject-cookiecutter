import asyncio

import asyncpg
from airflow.triggers.base import BaseTrigger, TriggerEvent


class AsyncPgSqlTrigger(BaseTrigger):
    """
    Асинхронный SQL-триггер для PostgreSQL без потоков.
    Использует asyncpg для неблокирующего опроса БД.
    """

    def __init__(
        self,
        conn_config: dict,
        sql: str,
        poke_interval: float = 60,
    ):
        super().__init__()
        self.conn_config = conn_config
        self.sql = sql
        self.poke_interval = poke_interval

    def serialize(self) -> tuple[str, dict]:
        class_path = f"{self.__class__.__module__}.{self.__class__.__qualname__}"
        return (
            class_path,
            {
                "conn_config": self.conn_config,
                "sql": self.sql,
                "poke_interval": self.poke_interval,
            },
        )

    async def run(self):
        conn = await asyncpg.connect(**self.conn_config)
        try:
            while True:
                records = None
                try:
                    records = await conn.fetch(self.sql)
                except asyncpg.exceptions.UndefinedTableError as e:
                    self.log.warning(f"Trigger fetch error: {e}")

                if records:
                    yield TriggerEvent(records)
                    return
                await asyncio.sleep(self.poke_interval)
        finally:
            await conn.close()
