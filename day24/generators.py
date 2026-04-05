def total_spent(self):
        return sum(expense.amount for expense in self.expenses)

def spending_by_category(self):
        spending_dict = {}
        for expense in self.expenses:
            spending_dict[expense.category] = spending_dict.get(expense.category, 0) + expense.amount
        return spending_dict