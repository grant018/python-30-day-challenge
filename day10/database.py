from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.orm import DeclarativeBase, Session

engine = create_engine("sqlite:///./media.db")

class Base(DeclarativeBase):
    pass

class Movie(Base):
    __tablename__ = "movies"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    genre = Column(String, default="undefined")
    year = Column(Integer, default=2000)
    available_to_rent = Column(Boolean, default=False)

class Song(Base):
    __tablename__ = "songs"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    artist = Column(String)
    year = Column(Integer)

Base.metadata.create_all(bind=engine)

db = Session(engine)
movie = Movie(title="Barry Lyndon", genre="drama", year=1974, available_to_rent=True)
movie_two = Movie(title="Once Upon A Time In The West", genre="western", year=1970)
song = Song(title="God Only Knows", artist="The Beach Boys", year=1964)
song_two = Song(title="Rain", artist="The Beatles", year=1963)

db.add(movie)
db.add(movie_two)
db.add(song)
db.add(song_two)
db.commit()
db.close()