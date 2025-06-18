from db.database import get_connection
from models.expense import Expense

def add_expense(expense: Expense):
    conn = get_connection()
    cursor=conn.cursor()

    cursor.execute('''
        INSERT INTO expenses (amount, category, description, date)
        VALUES (?,?,?,?)
    ''', (expense.amount, expense.category,expense.description,expense.date))

    conn.commit()
    conn.close()
    print("Expense saved successfully")

def get_all_expenses():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT amount, category, description, date FROM expenses")
    rows = cursor.fetchall()

    expenses = []
    for row in rows:
        expense = Expense(*row)
        expenses.append(expense)

    conn.close()
    return expenses