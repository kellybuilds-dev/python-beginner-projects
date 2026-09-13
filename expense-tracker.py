expenses = []

print("💰 Welcome to Kelly's Expense Tracker")

while True:
    print("\nWhat would you like to do?")
    print("1. Add expense")
    print("2. View expenses")
    print("3. View total")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        name = input("What did you spend money on? ")
        amount = float(input("How much did you spend? ₦"))

        expenses.append({
            "name": name,
            "amount": amount
        })

        print("✅ Expense added!")

    elif choice == "2":
        if not expenses:
            print("📭 No expenses recorded yet.")
        else:
            print("\n📋 Your Expenses:")

            for expense in expenses:
                print(f"- {expense['name']}: ₦{expense['amount']:.2f}")

    elif choice == "3":
        total = sum(expense["amount"] for expense in expenses)

        print(f"\n💵 Total spent: ₦{total:.2f}")

    elif choice == "4":
        print("👋 Thanks for using Kelly's Expense Tracker!")
        break

    else:
        print("❌ Invalid choice. Please choose 1, 2, 3, or 4.")
