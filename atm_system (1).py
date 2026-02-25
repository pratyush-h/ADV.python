balance = 1000
def check_balance():
    print(f"Your current balance is: ${balance}")
def deposit(amount):
    global balance
    balance += amount
    print(f"Deposited ${amount}. New balance: ${balance}")
def withdraw(amount):
    global balance
    if amount > balance:
        print("Insufficient funds!")
    else:
        balance -= amount
        print(f"Withdrew ${amount}. New balance: ${balance}")
def main():
    while True:
        print("\nATM Menu:")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            check_balance()
        elif choice == '2':
            amount = float(input("Enter deposit amount: "))
            deposit(amount)
        elif choice == '3':
            amount = float(input("Enter withdrawal amount: "))
            withdraw(amount)
        elif choice == '4':
            print("Thank you for using the ATM!")
            break
        else:
            print("Invalid choice. Try again.")
if __name__ == "__main__":
    main()