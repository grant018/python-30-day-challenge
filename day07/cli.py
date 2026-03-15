import click
from rich.console import Console
from rich.table import Table

from models import Task, PriorityTask, RecurringTask, Project
from storage import load_project, save_project

project_file = "tasks.json"
console = Console()

@click.group()
def cli():
    """Task Manager - A CLI tool for managing projects and tasks"""
    pass

@cli.command()
@click.argument("name")
def create(name):
    """Create a new project"""
    project = Project(name)
    save_project(project, project_file)
    console.print(f"[green]Project '{name}' created![/green]")

@cli.command()
@click.argument("title")
@click.option("--desc", default="", help="Task description")
@click.option("--type", "task_type", type=click.Choice(["task", "priority", "recurring" ]), default="task")
@click.option("--priority", type=click.Choice(["low", "medium", "high", "critical"]), default="medium")
@click.option("--recurrence", type=click.Choice(["daily", "weekly", "monthly"]), default="daily")
def add(title, desc, task_type, priority, recurrence):
    """Add a task to the project"""
    project = load_project("project", project_file)
    if task_type == "priority":
        task = PriorityTask(title, desc, priority)
    elif task_type == "recurring":
        task = RecurringTask(title, desc, recurrence)
    else:
        task = Task(title, desc)
    project.add_task(task)
    save_project(project, project_file)
    console.print(f"[green]Added: {task}[/green]")

@cli.command()
@click.argument("title")
def delete(title):
    """Delete a task from the project"""
    project = load_project("project", project_file)
    search_dict = [task for task in project.tasks if task.title.lower() != title.lower()]
    original_count = len(project.tasks)
    project.tasks = search_dict
    if len(project.tasks) < original_count:
        save_project(project, project_file)
        console.print(f"[green]Deleted: {title}[/green]")
    else:
        console.print(f"[red]Task {title} not found[/red]")

@cli.command()
@click.argument("completed_task")
def complete(completed_task):
    """Mark a task as completed"""
    project = load_project("project", project_file)
    found = False
    for task in project.tasks:
        if completed_task.lower() == task.title.lower():
            found = True
            task.complete()
            save_project(project, project_file)
            
    if not found:
        console.print("[red]Task not found.[/red]")

@cli.command()
def list_tasks():
    """List all tasks"""
    project = load_project("project", project_file)
    if not project.tasks:
        console.print("[yellow]No tasks yet.[/yellow]")
        return
    
    table = Table(title=f"{project.name} Tasks")
    table.add_column("#", style="dim")
    table.add_column("Title", style="bold")
    table.add_column("Type", style="cyan")
    table.add_column("Status")

    for i, task in enumerate(project.tasks, 1):
        status = "[green]DONE[/green]" if task.completed else "[red]TODO[/red]"
        task_type = type(task).__name__
        table.add_row(str(i), task.title, task_type, status)
    
    console.print(table)

@cli.command()
def percentage_complete():
    """Show percentage of projects completed"""
    project = load_project("project", project_file)
    console.print(f"[cyan]{project.percent_complete()}[/cyan]")


if __name__ == "__main__":
    cli()