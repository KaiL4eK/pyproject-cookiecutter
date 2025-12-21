from pydantic_settings import BaseSettings, SettingsConfigDict

# https://docs.pydantic.dev/latest/concepts/pydantic_settings/
class NotebookSettings(BaseSettings):
    """Application settings."""

    model_config = SettingsConfigDict(
        env_prefix = "APP_NB_",
        case_sensitive = False,
        # https://docs.pydantic.dev/latest/concepts/pydantic_settings/#dotenv-env-support
        env_file=".env",
        env_file_encoding="utf-8"
    )

    # Loads APP_NAME env
    name: str
