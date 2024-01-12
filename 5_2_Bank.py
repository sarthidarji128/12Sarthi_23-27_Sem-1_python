import Bank_mod  # Import the Bank_mod module for bank account functionality

# Create a bank account object with account number 12345 and initial balance 1000
account1 = Bank_mod.BankAccount(12345, 1000)

while True:  # Create an infinite loop for user interaction
    print("\nChoose an option:")
    print("1. Check balance")
    print("2. Withdraw money")
    print("3. Deposit money")
    print("4. Exit")

    choice = input("Enter your choice: ")  # Get user's choice

    if choice == "1":
        balance = account1.check_balance()  # Call check_balance method
        print("Your balance is:", balance)

    elif choice == "2":
        amount = float(input("Enter amount to withdraw: "))  # Get withdrawal amount
        try:
            balance = account1.withdraw(amount)  # Call withdraw method, handling potential errors
            print("Balance after withdrawal:", balance)
        except ValueError as e:
            print(e)  # Print any withdrawal errors

    elif choice == "3":
        amount = float(input("Enter amount to deposit: "))  # Get deposit amount
        try:
            balance = account1.deposit(amount)  # Call deposit method, handling potential errors
            print("Balance after deposit:", balance)
        except ValueError as e:
            print(e)  # Print any deposit errors

    elif choice == "4":
        print("Exiting...")
        break  # Exit the loop

    else:
        print("Invalid choice. Please try again.")
