from expense_tracker import add_expense, remove_expense, total_expense

def test_expense_tracker():
    add_expense('Food', 100)
    add_expense('Food', 50)
    assert total_expense('Food') == 150
    remove_expense('Food', 0)
    assert total_expense('Food') == 50
