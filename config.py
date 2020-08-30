from functools import lru_cache
import os
from pathlib import Path

from pydantic import BaseSettings
from dotenv import load_dotenv

app_path = '/Users/brandon/projects/fastapi-tutorial'


class Settings(BaseSettings):
    app_name: str = "Offroad Base"


def load_environment_files():
    environment = os.getenv('environment')
    common_env = Path(app_path) / 'common.env'
    environment_env = Path(app_path) / f'{environment}.env'
    return [common_env, environment_env]


def get_settings():
    common_env, environment_env = load_environment_files()

    load_dotenv(dotenv_path=common_env)
    load_dotenv(dotenv_path=environment_env)
    return Settings()
