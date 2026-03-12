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


task = Task("Learn OOP", "Understand classes and objects")
task_two = Task("Thing", "Understand classes and objects")
print(task)           # [✗] Learn OOP
task.complete()       # 'Learn OOP' marked complete!
print(task)           # [✓] Learn OOP
project = Project("Large Project")
project.add_task(task)
project.add_task(task_two)
project.list_tasks()
print(project.percent_complete())
