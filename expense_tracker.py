expenses = {}

def add_expense(category, amount):
    if amount <= 0:
        raise ValueError("Amount must be positive")
    if category not in expenses:
        expenses[category] = []
    expenses[category].append(amount)
    
def remove_expense(category, index):
    if category in expenses and 0 <= index < len(expenses[category]):
        expenses[category].pop(index)
    else:
        raise IndexError("Invalid expense index")

def total_expense(category):
    if category in expenses:
        return sum(expenses[category])
    return 0
