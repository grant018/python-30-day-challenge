from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_url: str = "sqlite:///./bookmarks.db"
    app_name: str = "Bookmark Manager"
    debug: bool = True
    api_version: str = "v1"
    host: str = "0.0.0.0"
    port: int = 8000

    class Config:
        env_file = ".env"

settings = Settings()