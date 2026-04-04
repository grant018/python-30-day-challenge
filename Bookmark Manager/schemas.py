from datetime import datetime
from pydantic import BaseModel
from typing import Optional

class TagResponse(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True

class BookmarkCreate(BaseModel):
    url: str
    title: str
    description: str = "no description"
    tags: list[str] = []

class BookmarkResponse(BaseModel):
    id: int
    url: str
    title: str
    description: str
    is_favorite: bool
    created_at: datetime
    tags: list[TagResponse] = []

    class Config:
        from_attributes = True

class BookmarkUpdate(BaseModel):
    url: Optional[str] = None
    title: Optional[str] = None
    description: Optional[str] = None
    is_favorite: Optional[bool] = None