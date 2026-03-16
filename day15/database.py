from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Session

engine = create_engine("sqlite:///./tasks.db")

class Base(DeclarativeBase):
    pass
