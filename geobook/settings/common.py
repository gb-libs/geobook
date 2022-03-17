import typing
from functools import lru_cache

from pydantic import AnyHttpUrl, BaseSettings

from .database import DatabaseSettings
from .jwt import JWTSettings
from .server import ServerSettings


class Settings(BaseSettings):
    TITLE: str
    DESCRIPTION: str
    VERSION: str
    SECRET: str
    CORS_ORIGINS: typing.List[AnyHttpUrl] = []

    SERVER: ServerSettings
    DATABASE: DatabaseSettings
    JWT: JWTSettings

    class Config:
        env_file = './config/.env'
        env_file_encoding = 'utf-8'
        case_sensitive = True
        env_nested_delimiter = '__'


@lru_cache()
def get_config() -> Settings:
    return Settings()
