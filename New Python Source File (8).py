attendance = {}
while True:
    choice = input("1. Add 2. Remove 3. Display 4. Exit: ")
    if choice == "1":
        name = input("Name: ")
        attendance[name] = "Present"
    elif choice == "2":
        attendance.pop(input("Name to remove: "), None)
    elif choice == "3":
        print(attendance)
    elif choice == "4":
        break