# Expense Tracker Project

expenses = []  # list of expenses as dictionaries
print("Welcome to Expense Tracker")

while True:
    print("\n=== MENU ===")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. View Total Expense")
    print("4. Exit")

    choice = int(input("Enter your choice (1-4): "))

    # Add Expense
    if choice == 1:
        date = input("Enter date (YYYY-MM-DD): ")
        category = input("Enter category (e.g. Food, Transport): ")
        description = input("Enter description: ")
        amount = float(input("Enter amount: "))

        expense = {
            "date": date,
            "category": category,
            "description": description,
            "amount": amount
        }

        expenses.append(expense)
        print("Expense added successfully!")

    # View Expenses
    elif choice == 2:
        if not expenses:
            print("No expenses recorded yet.")
        else:
            print("\n==== Expenses ====")
            for expense in expenses:
                print(
                    f"Date: {expense['date']}, "
                    f"{expense['category']} - {expense['description']}: "
                    f"₹{expense['amount']:.2f}"
                )

    # View Total Expense
    elif choice == 3:
        total = 0
        for expense in expenses:
            total += expense["amount"]
        print(f"\nTotal Expense: ₹{total:.2f}")

    # Exit
    elif choice == 4:
        print("Exiting Expense Tracker. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
