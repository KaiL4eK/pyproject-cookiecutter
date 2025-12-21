"""Settings module."""


from pydantic_settings import BaseSettings





class StreamlitAppSettings(BaseSettings):
    """Streamlit application settings."""

    class Config:
        env_prefix="STREAMLIT_APP_"
        case_sensitive=False

    create_all_tables: bool = False
