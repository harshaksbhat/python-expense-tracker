import sys

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
try:
    if option == 1:
        print("1. Add Expense")
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
        sys.exit(0)
    else:
        print("Invalid option Closing application")
except ValueError:
        print("Closing program")
        sys.exit(0)

