# List comprehension - create a new list by transforming another
numbers = [3, 5, 6, 8, 10, 22, 11]
evens = [n for n in numbers if n % 2 == 0]
squared = [n ** 2 for n in numbers]
print(f"Evens: {evens}")
print(f"Squared: {squared}")

# Dict comprehension
names = ["alice", "bob", "charlie"]
name_lengths = {name: len(name) for name in names}
print(f"Name lengths: {name_lengths}")

# Set operations
team_a = {"alice", "bob", "charlie", "diana"}
team_b = {"charlie", "diana", "eve", "frank"}
print(f"On both teams: {team_a & team_b}")
