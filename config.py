from functools import lru_cache
import os
from pathlib import Path

from pydantic import BaseSettings
from dotenv import load_dotenv

app_path = '/Users/brandon/projects/offroad-base'


class Settings(BaseSettings):
    app_name: str = "Offroad Base"
    app_path: str

    class Config:
        env_prefix = 'OFFROAD_BASE_' # Prefix env variables with this to replace the definition above


def load_environment_files():
    environment = os.getenv('environment')
    common_env = Path(app_path) / 'common.env'
    environment_env = Path(app_path) / f'{environment}.env'
    return [common_env, environment_env]


def get_settings():
    common_env, environment_env = load_environment_files()

    load_dotenv(dotenv_path=common_env)
    load_dotenv(dotenv_path=environment_env, override=True)
    print(Settings().dict())
    return Settings()
