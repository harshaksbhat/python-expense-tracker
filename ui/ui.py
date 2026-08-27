import sys
from expense.expense_manager import Input_Expense
while True:
    print("=========================================================================================================")
    print("                                        Expense Tracker                                                     ")
    print("=========================================================================================================")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Search by Category")
    print("4. Show Summary")
    print("5. Delete Expense")
    print("6. Exit")
    option = int(input("Choose your option: "))
    if option == 1:
        expense = Input_Expense()
        expense.input_expense()
        print("Expense Added")
    elif option == 2:
        print("2. View Expenses")
    elif option == 3:
        print("3. Search by Category")
    elif option == 4:
        print("4. Show Summary")
    elif option == 5:
        print("5. Delete Expense")
    elif option == 6:
        print("Exiting")
        break
    else:
        print("Invalid option Please select a valid option")
        continue

