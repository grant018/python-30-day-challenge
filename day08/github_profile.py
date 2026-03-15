import requests, time
from rich.console import Console
from rich.table import Table

console = Console()
username = console.input("[green]Please enter a Github username: [/green]")
table = Table(title=f"{username}'s Repos", style="bold")
table.add_column("Name", style="bold")
table.add_column("Description")

def timer(func):
    def wrapper():
        start_time = time.time()
        result = func()
        end_time = time.time()
        print(f"This operation took {(end_time - start_time):.1f} seconds to complete.")
        return result
    return wrapper

@timer
def repos_summary():
    try:
        r = requests.get(f"https://api.github.com/users/{username}")
        r_repos = requests.get(f"https://api.github.com/users/{username}/repos")
        data = r.json()
        data_repos = r_repos.json()
        console.print(f"[cyan]Name: {data['name']}[/cyan]")
        console.print(f"[cyan]Bio: {data['bio']}[/cyan]")
        console.print(f"[cyan]Total public repos: {data['public_repos']}[/cyan]")
        console.print(f"[cyan]Total followers: {data['followers']}\n[/cyan]")
        
        for repo in data_repos:
            table.add_row(repo['name'], repo['description'] or "No description")
        
        console.print(table)

    except KeyError:
        console.print("[red]Username not found.[/red]")

    except requests.exceptions.ConnectionError:
        console.print("[red]Could not connect to server.[/red]")

if __name__ == "__main__":
    repos_summary()