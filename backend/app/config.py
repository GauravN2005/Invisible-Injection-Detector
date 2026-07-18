from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "Invisible Injection Detector"
    VERSION: str = "1.0"
    MODEL_API: str = "http://localhost:8001/predict"
    LOG_PATH: str = "logs/app.log"


settings = Settings()