# src/config.py
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    # App Settings
    SECRET_KEY: str
    
    # Telegram Settings
    BOT_TOKEN: str
    WEBHOOK_URL: str
    
    # Database Settings
    DATABASE_URL: str

    # Automatically load from .env file
    model_config = SettingsConfigDict(
        env_file=".env", 
        env_file_encoding="utf-8",
        extra="ignore" # Ignores extra env vars you might have
    )

# Instantiate settings to be imported across the project
settings = Settings()