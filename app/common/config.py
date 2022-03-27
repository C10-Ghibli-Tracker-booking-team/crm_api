from pydantic import BaseSettings
import os


class Settings(BaseSettings):
    postgres_password: str
    postgres_port: str
    postgres_user: str
    postgres_db: str
    database_hostname: str

    class Config:
        environment_path = os.environ.get("ENV_STATE")
        if environment_path:
            env_file = "environments/production.env"
        else:
            env_file = "environments/development.env"


settings = Settings()
