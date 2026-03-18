from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from database import engine, Base
from models import Task
import logging

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger("main.py")

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Task Manager API")

class TaskCreate(BaseModel):
    title: str
    description: str = ""
    task_type: str = "task"

@app.get("/tasks")
def get_tasks():
    db = Session(engine)
    all_tasks = db.query(Task).all()
    logger.debug("Get all tasks requested")
    db.close()
    return all_tasks

@app.get("/tasks/{task_id}")
def get_task_by_id(task_id: int):
    db = Session(engine)
    get_task = db.query(Task).filter(Task.id == task_id).first()
    if get_task:
        logger.info(f"Task ID: {task_id} found.")
        db.close()
        return get_task
    db.close()
    logger.warning(f"Task ID: {task_id} can not be found")
    raise HTTPException(status_code=404, detail="Task not found")

@app.put("/tasks/{task_id}")
def update_task(task_id: int, task_update: TaskCreate):
    db = Session(engine)
    task_to_update = db.query(Task).filter(Task.id == task_id).first()
    if task_to_update:
        logger.info(f"Task ID: {task_id} found.")
        task_to_update.title = task_update.title
        task_to_update.description = task_update.description
        task_to_update.task_type = task_update.task_type
        logger.info(f"Task ID: {task_id} updated.")
        db.commit()
        db.close()
        return task_to_update
    db.close()
    logger.warning(f"Task ID: {task_id} can not be found")
    raise HTTPException(status_code=404, detail="Task not found")

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    db = Session(engine)
    delete_task = db.query(Task).filter(Task.id == task_id).first()
    if delete_task:
        logger.info(f"Task ID: {task_id} found.")
        db.delete(delete_task)
        logger.info(f"Task ID: {task_id} deleted.")
        db.commit()
        db.close()
        return {"message": f"ID: {delete_task.id} Task: {delete_task.title} has been deleted"}
    db.close()
    logger.warning(f"Task ID: {task_id} can not be found")
    raise HTTPException(status_code=404, detail="Task not found")

@app.patch("/tasks/{task_id}")
def complete_task(task_id: int):
    db = Session(engine)
    completed_task = db.query(Task).filter(Task.id == task_id).first()
    if completed_task:
        completed_task.completed = True
        db.commit()
        db.close()
        return {"message": f"{completed_task.title} has been marked complete."}
    logger.warning(f"Task ID: {task_id} can not be found")
    raise HTTPException(status_code=404, detail="Task not found")

@app.post("/tasks")
def create_task(task: TaskCreate):
    db = Session(engine)
    new_task = Task(
        title=task.title,
        description=task.description,
        task_type=task.task_type
        )
    db.add(new_task)
    db.commit()
    logger.info(f"New task {new_task.title} created")
    db.refresh(new_task)
    db.close()
    return new_task