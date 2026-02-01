from pydantic_settings import BaseSettings
from pydantic import PostgresDsn, Field

class Settings(BaseSettings):
    # These names must match your Infisical keys exactly
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    POSTGRES_HOST: str = "db"  # Matches the service name in docker-compose
    POSTGRES_PORT: int = 5433

    # Strava Credentials
    STRAVA_CLIENT_ID: str
    STRAVA_CLIENT_SECRET: str
    STRAVA_VERIFY_TOKEN: str  # A random string you create for webhook security

    @property
    def DATABASE_URL(self) -> str:
        return f"postgresql://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"

    class Config:
        env_file = None  # Infisical handles the injection

settings = Settings()