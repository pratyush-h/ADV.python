#Banking system with Transaction
import time

accounts = {
    "1001": 5000,
    "1002": 3000,
    "1003": 7000
}

TIME_LIMIT = 5

while True:
    print("\n--- Banking System ---")
    sender = input("Enter sender account number: ")
    receiver = input("Enter receiver account number: ")

    if sender not in accounts or receiver not in accounts:
        print("Error: Incorrect account number")
        continue

    start = time.time()

    amount = float(input("Enter amount to transfer: "))

    if time.time() - start > TIME_LIMIT:
        print("Transaction timeout")
        continue

    if accounts[sender] < amount:
        print("Error: Overdraft! Not enough balance")
        continue

    accounts[sender] -= amount
    accounts[receiver] += amount

    print("Transaction successful!")
    print("Sender Balance:", accounts[sender])
    print("Receiver Balance:", accounts[receiver])

    cont = input("Another transaction? (y/n): ")
    if cont.lower() != "y":
        break