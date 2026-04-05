names = ["alice", "bob", "charlie", "diana"]
numbers = [1, 2, 3, 4, 5]
words = ["hello", "world", "python", "is", "fun"]

cap_names = [name.capitalize() for name in names]
squared_numbers = [(num ** 2) for num in numbers]
over_three = [word for word in words if len(word) > 3]

students = ["Alice", "Bob", "Charlie"]
grades = [95, 82, 91]
fruits = ["apple", "banana", "cherry", "date"]
student_dict = {student: grade for student, grade in zip(students, grades)}

for index, fruit in enumerate(fruits, 1):
    print(f"Position: {index} Fruit: {fruit}")


