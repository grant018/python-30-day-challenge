import json
from models import Task, PriorityTask, RecurringTask, Project


def load_project(name: str, filename: str) -> Project:
    project = Project(name)
    try:
        with open(filename, "r") as f:
            data = json.load(f)
        for item in data:
            if item['type'] == "PriorityTask":
                project.tasks.append(PriorityTask.from_dict(item))
            elif item['type'] == "RecurringTask":
                project.tasks.append(RecurringTask.from_dict(item))
            else:
                project.tasks.append(Task.from_dict(item))
    except FileNotFoundError:
        pass
    return project

def save_project(project: Project, filename: str) -> None:
    task_list = [task.to_dict() for task in project.tasks]
    with open(filename, "w") as f:
        json.dump(task_list, f, indent=2)