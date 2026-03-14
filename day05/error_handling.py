class TaskError(Exception):
    """Base exception for task manager"""
    pass

class DuplicateTaskError(TaskError):
    """Raised when adding a task that already exists"""
    pass

class TaskNotFoundError(TaskError):
    """Raised when a task can't be found"""
    pass

tasks = ["cleaning", "scrubbing"]
def add_task(title: str) -> None:
    if title in tasks:
        raise DuplicateTaskError(f"'{title}' already exists!")
    tasks.append(title)
    print(f"Added '{title}'")

try:
    add_task("cleaning")
except DuplicateTaskError as e:
    print(f"Error: {e}")