from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict

class Config(BaseSettings):
    APP_NAME: str = "LLM Backend"
    DEBUG: bool = False
    PORT: int = 8000
    
    # CONFIG - DB
    DB_HOST: str
    DB_NAME: str
    DB_PASSWORD: SecretStr
    DB_PORT: int
    DB_USER: SecretStr
    DB_TYPE: str
    
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )

config = Config()