from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.environ.get("DATABASE_URL", "sqlite:///./tasks.db")
APP_NAME = os.environ.get("APP_NAME", "Task Manager")
DEBUG = os.environ.get("DEBUG", "false").lower() == "true"
SECRET_KEY = os.environ.get("SECRET_KEY", "change-me-in-production")
API_VERSION = os.environ.get("API_VERSION", "v1")
HOST = os.environ.get("HOST", "0.0.0.0")
PORT = int(os.environ.get("PORT", "8000"))