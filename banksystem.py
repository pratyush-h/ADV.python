# Bank transfer
balance = 0.0
transactions = []

PASSWORD = input("Set your password: ")

while True:
    print("\nWelcome to the Banking System")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. View Transaction History")
    print("5. Exit")

    choice = input("Choose an option (1-5): ")

    # Password required for transactions
    if choice in ['1', '2', '3', '4']:
        pwd = input("Enter password: ")
        if pwd != PASSWORD:
            print("Incorrect password. Transaction cancelled.")
            continue

    if choice == '1':
        amount = float(input("Enter amount to deposit: "))
        balance += amount
        transactions.append(f"Deposited: ${amount:.2f}")
        print("Deposit successful.")

    elif choice == '2':
        amount = float(input("Enter amount to withdraw: "))
        if amount > balance:
            print("Insufficient funds.")
        else:
            balance -= amount
            transactions.append(f"Withdrew: ${amount:.2f}")
            print("Withdrawal successful.")

    elif choice == '3':
        print(f"Current Balance: ${balance:.2f}")

    elif choice == '4':
        print("Transaction History:")
        if not transactions:
            print("No transactions yet.")
        for t in transactions:
            print(t)

    elif choice == '5':
        print("Thank you for using the Banking System. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")