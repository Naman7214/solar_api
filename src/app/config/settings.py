from pydantic_settings import BaseSettings
from typing import ClassVar

class Settings(BaseSettings):
    MODEL_PATH : str

    CLASS_NAMES: ClassVar[list[str]] = ["Bird-drop", "Clean", "Dusty", "Electrical-damage", "Physical-Damage", "Snow-Covered"]
    class Config:
        env_file = ".env"

settings = Settings()