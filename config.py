import os.path
from typing import Any, Dict, List, Optional, Union
from pydantic import AnyHttpUrl, BaseSettings, EmailStr, HttpUrl, PostgresDsn, validator


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_HOST = os.getenv('DB_HOST')
DB_USER=  os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_DATABASE = os.getenv('DB_DATABASE')
DB_PORT = os.getenv('DB_PORT')


class Settings(BaseSettings):
    API_STR: str = "/api"
    SERVER_NAME: str
    SERVER_HOST: AnyHttpUrl