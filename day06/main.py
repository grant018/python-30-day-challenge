from models import Task, RecurringTask, PriorityTask, Project
from storage import load_project, save_project

project = None
menu_selection = """
*** Welcome To Task Manager ***

1. Create New Project
2. Load Project
3. Save Project
4. Add Task
5. Complete Task
6. List Tasks
7. Percentage Completed
8. Exit

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
        if not project:
            print("No project loaded. Create or load one first.")
        else:
            save_project(project, f"{project.name}.json")
            print(f"{project.name} has been saved.")
    
    elif user_selection == "4":
        if not project:
            print("No project loaded. Create or load one first.")
        else:
            task_type = input("Please enter a task type (Task/Priority/Recurring): ").lower()
            task_name = input("Please enter a task name: ")
            task_description = input("Please enter a task description: ")
            if task_type == "task":
                task = Task(task_name, task_description)
                project.add_task(task)
                print(f"{task_name} has been added to {project.name}")
            elif task_type == "priority":
                priority_level = input("Priority level low/medium/high/critical: ").lower()
                is_valid = Task.is_valid_priority(priority_level)
                if is_valid:
                    task = PriorityTask(task_name, task_description, priority_level)
                    project.add_task(task)
                    print(f"{task_name} has been added to {project.name} with priority level {priority_level}")
                else:
                    print("Invalid priority selection")
            elif task_type == "recurring":
                accepted_recurrence = ['daily', 'weekly', 'monthly']
                recurrence = input("Please enter recurrence (Daily, Weekly, Monthly): ").lower()
                if recurrence in accepted_recurrence:
                    task = RecurringTask(task_name, task_description, recurrence)
                    project.add_task(task)
                    print(f"{task_name} has been added to {project.name} reoccuring {recurrence}")
                else:
                    print("Invalid recurrence selection")
        
    elif user_selection == "5":
        if not project:
            print("No project loaded. Create or load one first.")
        else:
            task_to_complete = input("Please enter a task name to mark complete: ")
            found = False
            for task in project.tasks:
                if task_to_complete.lower() == task.title.lower():
                    task.complete()
                    found = True
                    break
            if not found:
                print("Task not found.")
    
    elif user_selection == "6":
        if not project:
            print("No project loaded. Create or load one first.")
        else:
            project.list_tasks()
    
    elif user_selection == "7":
        if not project:
            print("No project loaded. Create or load one first.")
        else:
            print(project.percent_complete())

    elif user_selection == "8":
        break

    else:
        print("Invalid selection.")