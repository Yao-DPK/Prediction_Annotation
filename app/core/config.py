import os

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # Database configuration
    DATABASE_URL: str = os.getenv("DATABASE_URL", "postgresql://feedback_user:feedback_password@localhost:5433/feedback_db")
    
    # JWT Configuration
    SECRET_KEY: str = os.getenv("SECRET_KEY", "your_secret_key")  # Use a secure random string in production
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30  # Token expiration time in minutes

    # Other settings
    PROJECT_NAME: str = "TG Organization Backend"
    BACKEND_CORS_ORIGINS: list[str] = ["*"]  # Adjust to allow specific domains in production

    class Config:
        case_sensitive = True

# Instantiate settings
settings = Settings()
