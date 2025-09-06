"""Settings module."""


from pydantic_settings import BaseSettings


# https://docs.pydantic.dev/latest/concepts/pydantic_settings/
class AppSettings(BaseSettings):
    """Application settings."""

    class Config:
        env_prefix = "APP_"
        case_sensitive = False
        # https://docs.pydantic.dev/latest/concepts/pydantic_settings/#dotenv-env-support
        env_file=".env"
        env_file_encoding="utf-8"

    # Loads APP_NAME env
    name: str
