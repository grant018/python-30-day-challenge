from fastapi import FastAPI, HTTPException
from models import Bookmark, Tag, bookmark_tags
from database import engine, Base
from sqlalchemy.orm import Session
from schemas import BookmarkCreate, BookmarkResponse, BookmarkUpdate

Base.metadata.create_all(bind=engine)

app =FastAPI(title="Bookmark Manager API")

@app.post("/bookmarks", response_model=BookmarkResponse)
def create_bookmark(bookmark: BookmarkCreate):
    with Session(engine) as session:
        new_bookmark = Bookmark(
            url=bookmark.url,
            title=bookmark.title,
            description=bookmark.description
        )
        session.add(new_bookmark)
        for tag_name in bookmark.tags:
            tag = session.query(Tag).filter(Tag.name == tag_name).first()
            if not tag:
                tag = Tag(name=tag_name)
            new_bookmark.tags.append(tag)
        session.commit()
        session.refresh(new_bookmark)
        return new_bookmark

@app.get("/bookmarks", response_model=list[BookmarkResponse])
def get_bookmarks():
    with Session(engine) as session:
        all_bookmarks = session.query(Bookmark).all()
        return all_bookmarks

@app.get("/bookmarks/{bookmark_id}", response_model=BookmarkResponse)
def get_bookmark_by_id(bookmark_id: int):
    with Session(engine) as session:
        bookmark_found = session.query(Bookmark).filter(Bookmark.id == bookmark_id).first()
        if not bookmark_found:
            raise HTTPException(status_code=404, detail="Bookmark not found")
        return bookmark_found

@app.delete("/bookmarks/{bookmark_id}")
def bookmark_delete(bookmark_id: int):
    with Session(engine) as session:
        bookmark_to_delete = session.query(Bookmark).filter(Bookmark.id == bookmark_id).first()
        if not bookmark_to_delete:
            raise HTTPException(status_code=404, detail="Bookmark not found")
        session.delete(bookmark_to_delete)
        session.commit()
        return f"Bookmark: {bookmark_to_delete.url} ID: {bookmark_id} has been deleted successfully."

@app.put("/bookmarks/{bookmark_id}", response_model=BookmarkResponse)
def bookmark_update(bookmark_id: int, bookmark_update: BookmarkUpdate):
    with Session(engine) as session:
        bookmark_to_update = session.query(Bookmark).filter(Bookmark.id == bookmark_id).first()
        if not bookmark_to_update:
            raise HTTPException(status_code=404, detail="Bookmark not found")
        if bookmark_update.url is not None:
            bookmark_to_update.url = bookmark_update.url
        if bookmark_update.title is not None:
            bookmark_to_update.title = bookmark_update.title
        if bookmark_update.description is not None:
            bookmark_to_update.description = bookmark_update.description
        if bookmark_update.is_favorite is not None:
            bookmark_to_update.is_favorite = bookmark_update.is_favorite
        session.commit()
        session.refresh(bookmark_to_update)
        return bookmark_to_update
    
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)