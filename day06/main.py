from models import Task, RecurringTask, PriorityTask, Project
from storage import load_project, save_project

def is_loaded():
    if project:
        pass
    else:
        print("No project loaded.")
menu_selection = """
*** Welcome To Task Manager ***

1. Create New Project
2. Load Project
3. Save Project
4. Add Task
5. Delete Task
6. Complete Task
7. List Tasks
8. Status Summary
9. Percentage Completed

Please enter a selection: """

while True:
    user_selection = input(menu_selection)

    if user_selection == "1":
        project_name = input("Please enter a name for your project: ")
        project = Project(project_name)
        print(f"{project_name} has been created.")

    elif user_selection == "2":
        enter_file = input("Enter project filename: ")
        project = load_project(enter_file.replace(".json", ""), enter_file)
        print(f"{enter_file} has been loaded")
    
    elif user_selection == "3":
        save_project(project, f"{project.name}.json")
        print(f"{project.name} has been saved.")
    
    elif user_selection == "4":
        task_type = input("Please enter a task type (Task/Priority/Recurring): ").lower()
        task_name = input("Please enter a task name: ")
        task_description = input("Please enter a task description: ")
        if task_type == "task":
            task = Task(task_name, task_description)
            print(f"{task_name} has been added to {project.name}")
        elif task_type == "priority":
            priority_level = input("Priority level low/medium/high/critical: ").lower()
            is_valid = Task.is_valid_priority(priority_level)
            if is_valid:
                task = PriorityTask(task_name, task_description, priority_level)
                print(f"{task_name} has been added to {project.name} with priority level {priority_level}")
            else:
                print("Invalid priority selection")
        elif task_type == "recurring":
            accepted_recurrence = ['daily', 'weekly', 'monthly']
            recurrence = input("Please enter recurrence (Daily, Weekly, Monthly): ").lower()
            if recurrence in accepted_recurrence:
                task = RecurringTask(task_name, task_description, recurrence)
                print(f"{task_name} has been added to {project.name} reoccuring {recurrence}")
            else:
                print("Invalid recurrence selection")
        