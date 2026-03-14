import json

class Task:
    def __init__(self, title: str, description: str = ""):
        self.title = title
        self.description = description
        self.completed = False
    
    def complete(self):
        self.completed = True
        print(f"'{self.title}' marked complete!")
    
    def to_dict(self) -> dict:
        return {
            "type": "Task",
            "title": self.title,
            "description": self.description,
            "completed": self.completed
        }
    
    def __str__(self) -> str:
        status = "DONE" if self.completed else "TODO"
        return f"[{status}] {self.title}"
    
    def __repr__(self):
        return f"Task('{self.title}', '{self.description}')"
    
    def __eq__(self, other) -> bool:
        return self.title == other.title and self.description == other.description

    
    @classmethod
    def from_dict(cls, data: dict):
        task = cls(data['title'], data['description'])
        task.completed = data['completed']            
        return task
    
    @classmethod
    def from_string(cls, task_string: str):
        """Create a Task from a string like 'title|description'"""
        title, description = task_string.split("|")
        return cls(title.strip(), description.strip())
    
    @staticmethod
    def is_valid_priority(priority: str) -> bool:
        return priority.lower() in {"low", "medium", "high", "critical"}

  
class PriorityTask(Task):
    def __init__(self, title: str, description: str = "", priority: str = "medium"):
        super().__init__(title, description)
        self.priority = priority
    
    def to_dict(self):
        data = super().to_dict()
        data['type'] = "PriorityTask"
        data['priority'] = self.priority
        return data
    
    def __str__(self) -> str:
        status = "DONE" if self.completed else "TODO"
        return f"[{status}] [{self.priority.upper()}] {self.title}"

    @classmethod
    def from_dict(cls, data: dict):
        task = cls(data['title'], data['description'], data['priority'])
        task.completed = data['completed']
        return task
        

class RecurringTask(Task):
    def __init__(self, title: str, description: str = "", recurrence = "daily"):
        super().__init__(title, description)
        self.recurrence = recurrence
    
    def to_dict(self):
        data = super().to_dict()
        data['type'] = "RecurringTask"
        data['recurrence'] = self.recurrence
        return data
    
    def complete(self):
        super().complete()
        self.completed = False
        print(f"'{self.title}' reset - recurs {self.recurrence}")

    def __str__(self) -> str:
        status = "DONE" if self.completed else "TODO"
        return f"[{status}] [{self.recurrence}] {self.title}"

    @classmethod
    def from_dict(cls, data: dict):
        task = cls(data['title'], data['description'], data['recurrence'])
        task.completed = data['completed']
        return task

class Project:
    def __init__(self, name: str):
        self.name = name
        self.tasks = []
    
    def add_task(self, task: Task) -> None:
        self.tasks.append(task)
        print(f"{task.title} has been added to project tasks list")

    def list_tasks(self) -> None:
        for count, task in enumerate(self.tasks, 1):
            print(f"Task {count}: {task.title}: {task.description} Status: {task}")

    def percent_complete(self) -> str:
        if not self.tasks:
            return f"Project: {self.name} is 0.0% complete"
        count = sum(1 for task in self.tasks if task.completed)
        return f"Project: {self.name} is {(count / len(self.tasks)) * 100:.1f}% complete"

    @property
    def status_summary(self) -> str:
        total = len(self.tasks)
        done = sum(1 for task in self.tasks if task.completed)
        return f"{self.name}: {done}/{total} tasks complete"