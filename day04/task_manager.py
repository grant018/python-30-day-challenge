class Task:
    def __init__(self, title: str, description: str = ""):
        self.title = title
        self.description = description
        self.completed = False
    
    def complete(self):
        self.completed = True
        print(f"'{self.title}' marked complete!")
    
    def __str__(self) -> str:
        status = "DONE" if self.completed else "TODO"
        return f"[{status}] {self.title}"
    
    def __repr__(self):
        return f"Task('{self.title}', '{self.description}')"
    
    def __eq__(self, other) -> bool:
        return self.title == other.title and self.description == other.description

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
    
    def __str__(self) -> str:
        status = "DONE" if self.completed else "TODO"
        return f"[{status}] [{self.priority.upper()}] {self.title}"

class RecurringTask(Task):
    def __init__(self, title: str, description: str = "", recurrence = "daily"):
        super().__init__(title, description)
        self.recurrence = recurrence
    
    def complete(self):
        super().complete()
        self.completed = False
        print(f"'{self.title}' reset - recurs {self.recurrence}")

    def __str__(self) -> str:
        status = "DONE" if self.completed else "TODO"
        return f"[{status}] [{self.recurrence}] {self.title}"

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

project = Project("Project")
regular = Task("Buy groceries")
urgent = PriorityTask("Fix production bug", "Server is down", "high")
recurring = RecurringTask("Drink water")
project.add_task(regular)
project.add_task(urgent)
project.add_task(recurring)
urgent.complete()
print(project.status_summary)
print(Task.is_valid_priority("critiCal"))
test_task = Task.from_string("Mowing Lawn | Getting the grass cut")
project.add_task(test_task)
print(project.status_summary)