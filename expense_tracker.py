expenses = {}

def add_expense(category, amount):
    if category not in expenses:
        expenses[category] = []
    expenses[category].append(amount)

def remove_expense(category, index):
    if category in expenses and 0 <= index < len(expenses[category]):
        expenses[category].pop(index)

def total_all_expenses():
    return sum(sum(vals) for vals in expenses.values())
