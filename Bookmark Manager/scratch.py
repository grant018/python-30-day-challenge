from sqlalchemy import create_engine, Table, Column, String, Integer, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Session, relationship

engine = create_engine("sqlite:///./test.db")

class Base(DeclarativeBase):
    pass

actor_movies = Table(
    "actor_movies",
    Base.metadata,
    Column("movie_id", Integer, ForeignKey("movies.id")),
    Column("actor_id", Integer, ForeignKey("actors.id")),
)

class Movie(Base):
    __tablename__ = "movies"
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    genre = Column(String, default="not defined")
    actors = relationship("Actor", secondary=actor_movies, back_populates="movies")

class Actor(Base):
    __tablename__ = "actors"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    movies = relationship("Movie", secondary=actor_movies, back_populates="actors")

Base.metadata.create_all(bind=engine)

harrison_ford = Actor(name="Harrison Ford")
robert_mitchum = Actor(name="Robert Mitchum")
cary_grant = Actor(name="Cary Grant")
indiana_jones = Movie(title="Indiana Jones", genre="Action")
air_force_one = Movie(title="Air Force One", genre="Action")
north_by_northwest = Movie(title="North By Northwest", genre="Suspense")
night_of = Movie(title="Night Of The Hunter", genre="Drama")
north_by_northwest.actors.append(cary_grant)
air_force_one.actors.append(harrison_ford)
night_of.actors.append(robert_mitchum)
indiana_jones.actors.append(harrison_ford)

with Session(engine) as session:
    session.add_all([harrison_ford, robert_mitchum, cary_grant, air_force_one, indiana_jones, night_of, north_by_northwest])
    session.commit()
    movies = session.query(Movie).all()
    for movie in movies:
        print(f"{movie.title} - {movie.genre}:")
        for actor in movie.actors:
            print(f"{actor.name}")

