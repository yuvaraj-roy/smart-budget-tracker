from cProfile import label

import matplotlib.pyplot as plt
from collections import defaultdict

from unicodedata import category


def plot_expenses_by_category(expenses):
    category_totals = defaultdict(float)
    for expense in expenses:
        category_totals[expense.category.capitalize()] += expense.amount
    if not category_totals:
        print("No expense to display in chart.")
        return

    labels = list(category_totals.keys())
    values = list(category_totals.values())

    plt.figure(figsize=(6,6))
    plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.title("Expenses by Category")
    plt.axis('equal')
    plt.tight_layout()
    plt.show()