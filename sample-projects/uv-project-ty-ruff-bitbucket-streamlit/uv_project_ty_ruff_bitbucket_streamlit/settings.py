from pydantic import SecretStr, computed_field
from pydantic_settings import BaseSettings


# https://docs.pydantic.dev/latest/concepts/pydantic_settings/
class AppSettings(BaseSettings):
    class Config:
        env_prefix = "APP_"
        case_sensitive = False
        # https://docs.pydantic.dev/latest/concepts/pydantic_settings/#dotenv-env-support
        env_file='.env'
        env_file_encoding='utf-8'

    # Loads APP_NAME env
    name: str


class DatabaseSettings(BaseSettings):
    class Config:
        env_prefix="DATABASE_"
        case_sensitive=False

    host: str = "postgres"
    port: int = 5432
    username: str
    password: SecretStr

    name: str

    echo: bool = False

    @computed_field
    @property
    def sqlalchemy_uri_sync(self) -> dict:
        uri = f"postgresql+psycopg://{self.username}:{self.password.get_secret_value()}@{self.host}:{self.port}/{self.name}"
        return uri


class StreamlitAppSettings(BaseSettings):
    class Config:
        env_prefix="STREAMLIT_APP_"
        case_sensitive=False

    create_all_tables: bool = False
