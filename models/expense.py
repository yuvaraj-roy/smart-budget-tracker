from datetime import datetime

class Expense:
    def __init__(self,amount,category,description="",date=None):
        self.amount=amount
        self.category=category
        self.description=description
        self.date=date if date else datetime.now().strftime("%Y-%m-%d")

    def __repr__(self):
        return f"[${self.amount}] {self.category} - {self.description} ({self.date})"