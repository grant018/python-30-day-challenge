import json
from datetime import date

class Expense:
    def __init__(self, amount, category, description, expense_date=None):
        self.amount = amount
        self.category = category
        self.description = description
        self.expense_date = expense_date or date.today()
    
class BudgetTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, amount: float, category: str, description: str, expense_date=None):
        new_expense = Expense(amount, category, description, expense_date)
        self.expenses.append(new_expense)
        return new_expense
    
    def view_expenses(self):
        for expense in self.expenses:
            print(f"Amount: ${expense.amount:.2f} | Category: {expense.category} | Description: {expense.description} | Date: {expense.expense_date}")
    
    def total_spent(self):
        total = 0
        for expense in self.expenses:
            total += expense.amount
        return total
    
    def spending_by_category(self):
        spending_dict = {}
        for expense in self.expenses:
            spending_dict[expense.category] = spending_dict.get(expense.category, 0) + expense.amount
        return spending_dict

    def load_from_file(self, filename):
        try:
            with open(filename, "r") as file:
                data = json.load(file)
            for expense in data:
                self.add_expense(expense["amount"], expense["category"], expense["description"], expense["date"])
        except FileNotFoundError:
            return None

    def save_to_file(self, filename):
        expenses = []
        for expense in self.expenses:
            expenses.append({
                "amount": expense.amount,
                "category": expense.category,
                "description": expense.description,
                "date": str(expense.expense_date)
            })
        with open(filename, "w") as file:
            json.dump(expenses, file, indent=2)

menu = """
Budget Tracker CLI

1. Add Expense
2. View Expenses
3. View Total
4. View By Category
5. Quit

Please enter a selection: """

def main():

    budget_tracker = BudgetTracker()
    budget_tracker.load_from_file("budget_tracker.json")

    while True:
        selection = input(menu)

        if selection == "1":
            amount = float(input("Please enter an amount: "))
            category = input("Please enter a category: ").capitalize()
            description = input("Please enter a description: ").capitalize()

            budget_tracker.add_expense(amount, category, description)
            budget_tracker.save_to_file("budget_tracker.json")

        elif selection == "2":
            budget_tracker.view_expenses()

        elif selection == "3":
            print(f"Total Spent: ${budget_tracker.total_spent():.2f}")
        
        elif selection == "4":
            spending_by_category = budget_tracker.spending_by_category()
            for category, amount in spending_by_category.items():
                print(f"Category: {category} | Amount: ${amount:.2f}")
        
        elif selection == "5":
            break

        else:
            print("Invalid selection")


if __name__ == "__main__":
    main()
        

