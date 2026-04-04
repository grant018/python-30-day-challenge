from sqlalchemy import Table, Column, String, Integer, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from database import Base
from datetime import datetime

bookmark_tags = Table(
    "bookmark_tags",
    Base.metadata,
    Column("bookmark_id", Integer, ForeignKey("bookmarks.id")),
    Column("tag_id", Integer, ForeignKey("tags.id")),
)

class Bookmark(Base):
    __tablename__ = "bookmarks"
    id = Column(Integer, primary_key=True)
    url = Column(String, nullable=False)
    title = Column(String, nullable=False)
    description = Column(String, default="No description")
    is_favorite = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.now)

    tags = relationship("Tag", secondary=bookmark_tags, back_populates="bookmarks", lazy="joined")

class Tag(Base):
    __tablename__ = "tags"
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)

    bookmarks = relationship("Bookmark", secondary=bookmark_tags, back_populates="tags", lazy="joined")