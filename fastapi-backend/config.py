from functools import lru_cache

from pydantic import BaseSettings


@lru_cache()
def get_settings():
    return Settings()


class Settings(BaseSettings):
    sql_database_host: str = "localhost"
    sql_database_port: str = "5432"
    sql_database_user: str = "postgres"
    sql_database_password: str = "postgres"
    env: str = "DEV"

    class Config:
        env_file = ".env"
