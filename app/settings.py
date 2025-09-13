from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    # Project metadata
    PROJECT_NAME: str = "FastAPI Demo"
    PROJECT_VERSION: str = "1.0.0"
    PROJECT_DESCRIPTION: str = "A demo FastAPI application"
    
    # Debug settings
    DEBUG: bool = False
    
    # Database settings (example)
    DATABASE_URL: Optional[str] = None
    
    # API settings
    API_V1_STR: str = "/api/v1"
    
    # CORS settings
    BACKEND_CORS_ORIGINS: list = []
    
    class Config:
        case_sensitive = True
        env_file = ".env"


settings = Settings()
