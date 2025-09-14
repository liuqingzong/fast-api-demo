import os
from functools import lru_cache
from pydantic_settings import BaseSettings
from typing import List,Any

os.environ["ENV"] = "test"  # 设置环境变量以加载测试配置

class Settings(BaseSettings):
    """应用配置类"""
    APP_NAME: str = "fast-api-demo"
    APP_ENV: str = "development"
    APP_HOST: str = "0.0.0.0"
    APP_PORT: int = 8000

    class Config:
        running_env = os.getenv("ENV", None)
        env_file = ".env"
        if(running_env != None):
            env_file = (".env",f".env.{running_env}")


@lru_cache
def get_settings():
    return Settings()

settings = get_settings()