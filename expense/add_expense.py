import json

class AddExpense:
    def adding_expense(self):
        title = input("Enter Expense Title: ")
        amount = float(input("Enter Expense Amount: "))
        category = input("Enter Expense Category: ")

        expense = {
            "title": title,
            "amount": amount,
            "category": category
        }

        try:
            with open("../data/expenses.json", "r") as file:
                expenses = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            expenses = []

        expenses.append(expense)

        with open("../data/expenses.json", "w") as file:
            json.dump(expenses, file, indent=4)