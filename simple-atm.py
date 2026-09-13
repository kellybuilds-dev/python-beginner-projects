print("🏦 Welcome to Simple ATM")

balance = 50000
pin = "1234"

entered_pin = input("Enter your PIN: ")

if entered_pin == pin:
    print("\nLogin successful!")

    while True:
        print("\n--- ATM MENU ---")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            print(f"Your balance is ₦{balance}")

        elif choice == "2":
            amount = float(input("Enter deposit amount: ₦"))
            balance += amount
            print(f"Deposit successful. New balance: ₦{balance}")

        elif choice == "3":
            amount = float(input("Enter withdrawal amount: ₦"))

            if amount <= balance:
                balance -= amount
                print(f"Withdrawal successful. New balance: ₦{balance}")
            else:
                print("Insufficient balance.")

        elif choice == "4":
            print("Thank you for using Simple ATM. Goodbye! 👋")
            break

        else:
            print("Invalid option. Please try again.")

else:
    print("Incorrect PIN. Access denied.")
