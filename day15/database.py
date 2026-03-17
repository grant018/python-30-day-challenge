from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Session

DATABASE_URL = "postgresql://taskuser:taskpass@db:5432/taskdb"

engine = create_engine(DATABASE_URL)

class Base(DeclarativeBase):
    pass
