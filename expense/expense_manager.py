import json

class Add_Expense:
    '''
    This class adds expenses is used to add expenses to JSON File
    '''
    def add_expense(self, total_expense):
        try:
            with open("../data/expenses.json", "r") as file:
                expenses = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            expenses = []

        expenses.append(total_expense)

        with open("../data/expenses.json", "w") as file:
            json.dump(expenses, file, indent=4)

class Input_Expense(Add_Expense):
    '''
    Here the class Input_Expense Inherits Add_Expense class and its method to add the data to JSON
    '''

    def input_expense(self):
        title = input("Enter Expense Title: ")
        try:
            amount = float(input("Enter Expense Amount: "))
        except ValueError:
            print("Enter a valid amount.")
            return None
        if amount<=0:
            print("Enter valid amount")
            return None
        category = input("Enter Expense Category: ")

        total_expense = {
            "title": title,
            "amount": amount,
            "category": category
        }
        self.add_expense(total_expense)
        return total_expense


# class EditExpense(Expense):
#     data=input("Enter Expense Title: ")
#     add_expense=input("Enter Expense Amount: ")