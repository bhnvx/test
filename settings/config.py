import secrets
from functools import lru_cache
from pydantic import BaseSettings


class Settings(BaseSettings):
    SECRET_KEY: str = secrets.token_urlsafe(32)

    class Config:
        case_sensitive = True


@lru_cache
def get_config():
    return Settings()