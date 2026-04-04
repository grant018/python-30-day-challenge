from dotenv import load_dotenv
import os

load_dotenv()

db_url = os.environ.get("DATABASE_URL")
secret = os.environ.get("SECRET_KEY")
app_name = os.environ.get("APP_NAME")

print(f"Database: {db_url}")
print(f"Secret: {secret}")
print(f"App Name: {app_name}")
