import json
import logging
import os

from airflow import settings
from airflow.models import Connection


logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)-8s] %(name)s:%(lineno)d | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger(__name__)


def add_connection(conn_id: str, conn_cfg: str, overwrite: bool = False):
    """
    Add or update an Airflow connection.

    This function creates a new connection or updates an existing one based on the provided
    configuration. The configuration can be specified as a URI string or a JSON object.

    Args:
        conn_id (str): The unique identifier for the connection.
        conn_cfg (str): The connection configuration. Can be:
            - A URI string (e.g., 'postgres://user:pass@host:port/db')
            - A JSON string containing connection properties as a dictionary, e.g.:
              {
                "conn_type": "postgres",
                "description": "Sample PostgreSQL connection",
                "login": "username",
                "password": "password",
                "host": "localhost",
                "port": 5432,
                "schema": "public",
                "extra": {"sslmode": "require"}
              }
        overwrite (bool): If True, update the connection if it already exists.
                         If False (default), skip creation if the connection exists.

    Raises:
        ValueError: If the JSON configuration is not a valid dictionary.

    Examples:
        >>> add_connection("my_postgres", "postgres://user:pass@localhost:5432/mydb")
        >>> add_connection("my_postgres", '{"conn_type": "postgres", "host": "localhost"}', overwrite=True)
    """
    session = settings.Session()
    existing = session.query(Connection).filter(Connection.conn_id == conn_id).first()

    is_update = existing is not None and overwrite

    if existing and not overwrite:
        logger.info(f"Connection '{conn_id}' already exists, skipping creation.")
        session.close()
        return

    action = "Updating" if is_update else "Creating"
    logger.info(f"{action} connection: {conn_id} = {conn_cfg}")

    if not existing:
        existing = Connection(conn_id=conn_id)
        session.add(existing)

    # Set the configuration
    try:
        cfg = json.loads(conn_cfg)
        if isinstance(cfg, dict):
            for key, value in cfg.items():
                setattr(existing, key, value)
        else:
            raise ValueError("JSON configuration must be a dictionary")
    except json.JSONDecodeError:
        # Treat as URI
        existing.uri = conn_cfg

    session.commit()
    logger.info(f"Connection {conn_id} {'updated' if is_update else 'added'}.")
    session.close()


def add_connection_from_env(env_name, conn_id, overwrite: bool = False):
    raw = os.getenv(env_name)
    if not raw:
        raise RuntimeError(f"Environment variable '{env_name}' is not set")
    add_connection(conn_id=conn_id, conn_cfg=raw, overwrite=overwrite)


def main():
    add_connection_from_env("AIRFLOW_SAMPLE_POSTGRES_CONNECTION", "sample_postgres_connection")


if __name__ == "__main__":
    main()
