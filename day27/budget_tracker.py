import json
from datetime import date

class Expense:
    """An expense object that keeps track of the amount, category, description, and date of the expense"""
    def __init__(self, amount: float, category: str, description: str, expense_date=None):
        self.amount = amount
        self.category = category
        self.description = description
        self.expense_date = expense_date or date.today()
    
    def __str__(self):
        return f"Amount: ${self.amount:.2f} | Category: {self.category} | Description: {self.description} | Date: {self.expense_date}"
    
class BudgetTracker:
    """A budget tracker for adding and reviewing expenses + saving and loading expense data"""
    def __init__(self):
        self.expenses = []

    def add_expense(self, amount: float, category: str, description: str, expense_date=None) -> Expense:
        """Adds new expense to BudgetTracker object"""
        new_expense = Expense(amount, category, description, expense_date)
        self.expenses.append(new_expense)
        return new_expense
    
    def view_expenses(self) -> None:
        """Prints all expenses"""
        for expense in self.expenses:
            print(expense)
    
    def total_spent(self) -> float:
        """Returns total of expenses in self.expenses"""
        return sum(expense.amount for expense in self.expenses)
    
    def spending_by_category(self) -> dict[str, float]:
        """Returns a dictionary of total expenses for each category"""
        spending_dict = {}
        for expense in self.expenses:
            spending_dict[expense.category] = spending_dict.get(expense.category, 0) + expense.amount
        return spending_dict

    def load_from_file(self, filename: str) -> None:
        """Loads json containing expense data if it exists"""
        try:
            with open(filename, "r") as file:
                data = json.load(file)
            for expense in data:
                self.add_expense(expense["amount"], expense["category"], expense["description"], expense["date"])
        except FileNotFoundError:
            return None

    def save_to_file(self, filename: str) -> None:
        """Saves all expense data"""
        expenses = [{"amount": e.amount, "category": e.category,
                     "description": e.description, "date": str(e.expense_date)}
                    for e in self.expenses]
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
    """Main loop"""
    budget_tracker = BudgetTracker()
    budget_tracker.load_from_file("budget_tracker.json")

    while True:
        selection = input(menu)

        if selection == "1":
            while True:
                try:
                    amount = float(input("Please enter an amount: "))
                    category = input("Please enter a category: ").capitalize()
                    description = input("Please enter a description: ").capitalize()
                    break
                except ValueError:
                    print("Invalid entry")
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
        

