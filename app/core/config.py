import os
from typing import Optional

from pydantic import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "Book App"

    class Config:
        case_sensitive = True


settings = Settings()
