from pydantic_settings import BaseSettings, SettingsConfigDict


class AppSettings(BaseSettings):
    """Streamlit application settings."""

    model_config = SettingsConfigDict(
        env_prefix="STREAMLIT_APP_",
        case_sensitive=False
    )

    create_all_tables: bool = False
