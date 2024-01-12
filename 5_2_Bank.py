import Bank_mod
account1 =Bank_mod.BankAccount(12345, 1000)
while True:
    print("\nChoose an option:")
    print("1. Check balance")
    print("2. Withdraw money")
    print("3. Deposit money")
    print("4. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        balance = account1.check_balance()
        print("Your balance is:", balance)
    elif choice == "2":
        amount = float(input("Enter amount to withdraw: "))
        try:
            balance = account1.withdraw(amount)
            print("Balance after withdrawal:", balance)
        except ValueError as e:
            print(e)
    elif choice == "3":
        amount = float(input("Enter amount to deposit: "))
        try:
            balance = account1.deposit(amount)
            print("Balance after deposit:", balance)
        except ValueError as e:
            print(e)
    elif choice == "4":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")
