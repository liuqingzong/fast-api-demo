import os
from functools import lru_cache
from pydantic_settings import BaseSettings,SettingsConfigDict

# os.environ["ENV"] = "test"  # 设置环境变量以加载测试配置

class Settings(BaseSettings):
    """应用配置类"""
    APP_NAME: str = "fast-api-demo"
    APP_ENV: str = "development"
    APP_HOST: str = "0.0.0.0"
    APP_PORT: int = 8000

    # 日志配置
    LOG_LEVEL: str = "info"
    LOG_FILE_PATH: str = "./logs/app.log"

    class Config:
        print("加载文件")
        running_env = os.getenv("ENV", None)
        print(running_env)
        env_file = "../.env"
        if(running_env != None):
            env_file = ("../.env",f"../.env.{running_env}")
        print(env_file)
        model_config = SettingsConfigDict(env_file=env_file, env_file_encoding="utf-8")


def get_settings():
    return Settings()

settings = get_settings()
print(settings)