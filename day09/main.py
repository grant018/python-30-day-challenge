from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Task Manager API")

tasks = []
task_id_counter = 1

class TaskCreate(BaseModel):
    title: str
    description: str = ""
    task_type: str = "task"
    priority: str = "medium"
    recurrence: str = "daily"

class TaskResponse(BaseModel):
    id: int
    title: str
    description: str
    task_type: str
    completed: bool

@app.get("/tasks")
def get_tasks():
    return tasks

@app.get("/tasks/{task_id}")
def get_task_by_id(task_id: int):
    for task in tasks:
        if task['id'] == task_id:
            return task
    raise HTTPException(status_code=404, detail="Task not found")

@app.put("/tasks/{task_id}")
def update_task(task_id: int, task_update: TaskCreate):
    for task in tasks:
        if task['id'] == task_id:
            task['title'] = task_update.title
            task['description'] = task_update.description
            task['task_type'] = task_update.task_type
            return task
    raise HTTPException(status_code=404, detail="Task not found")

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    for task in tasks:
        if task['id'] == task_id:
            tasks.remove(task)
            return {"message": f"Task {task_id} deleted"}
    raise HTTPException(status_code=404, detail="Task not found")

@app.patch("/tasks/{task_id}")
def complete_task(task_id: int):
    for task in tasks:
        if task['id'] == task_id:
            task['completed'] = True
            return {"message": f"Task {task_id} has been marked complete."}
    raise HTTPException(status_code=404, detail="Task not found")

@app.post("/tasks")
def create_task(task: TaskCreate):
    global task_id_counter
    new_task = {
        "id": task_id_counter,
        "title": task.title,
        "description": task.description,
        "task_type": task.task_type,
        "completed": False
    }
    tasks.append(new_task)
    task_id_counter += 1
    return new_task