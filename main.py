from itertools import count

from unicodedata import category

from db.database import initialize_db
from models.expense import Expense
from services.expense_services import add_expense, get_all_expenses
from visualizations.expense_charts import plot_expenses_by_category
from datetime import date


def main():
    print("\n---Smart Budget Tracker---")
    initialize_db()

    while True:
        try:
            amount_input=input("Enter amount: $ ").strip()
            amount = float(amount_input)
        except ValueError:
            print(" Invalid input! Please enter a valid number for amount.\n")
            continue

        category = input("Entry category (e.g., Food, Travel): ")
        description = input("Enter description (optional): ")

        expense = Expense(
            amount=amount,
            category=category,
            description=description,
            date=date.today()

        )
        add_expense(expense)
        print("Expense saved successfully")

        cont = input("\nAdd another? ('y' to add another expense (or) 'n' to stop ): ").strip().lower()
        if cont != 'y':
            break

    print("\n--- All Expense ---")
    expenses = get_all_expenses()
    for exp in expenses:
        print(f"[${exp.amount}]{exp.category} - {exp.description} ({exp.date})")
        plot_expenses_by_category(expenses)

if __name__ == "__main__":
    main()