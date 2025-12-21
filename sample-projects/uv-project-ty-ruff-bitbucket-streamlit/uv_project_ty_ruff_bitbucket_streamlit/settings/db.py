from pydantic import SecretStr, computed_field
from pydantic_settings import BaseSettings, SettingsConfigDict


class DatabaseSettings(BaseSettings):
    """Database settings."""

    model_config = SettingsConfigDict(env_prefix="DATABASE_", case_sensitive=False)

    host: str = "postgres"
    port: int = 5432
    username: str
    password: SecretStr

    name: str

    echo: bool = False

    @computed_field
    @property
    def sqlalchemy_uri_async(self) -> str:
        """Return SQLAlchemy URI string representation."""
        uri = f"postgresql+asyncpg://{self.user}:{self.password.get_secret_value()}@{self.host}:{self.port}/{self.name}"
        return uri

    @computed_field
    @property
    def sqlalchemy_uri_sync(self) -> dict:
        """Return SQLAlchemy URI string representation."""
        uri = f"postgresql+psycopg://{self.username}:{self.password.get_secret_value()}@{self.host}:{self.port}/{self.name}"
        return uri
