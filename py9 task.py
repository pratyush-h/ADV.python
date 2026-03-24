
students = []

def add_student():
    sid = int(input("Enter ID: "))
    name = input("Enter Name: ")
    students.append([sid, name])
    print("Student added successfully!\n")

def view_students():
    print("\nStudent Records:")
    for s in students:
        print("ID:", s[0], "Name:", s[1])
    print()

def delete_student():
    sid = int(input("Enter ID to delete: "))
    for s in students:
        if s[0] == sid:
            students.remove(s)
            print("Student deleted successfully!\n")
            return
    print("Student not found!\n")

while True:
    print("----- MENU -----")
    print("1. Add Student")
    print("2. View Students")
    print("3. Delete Student")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        add_student()
    elif choice == 2:
        view_students()
    elif choice == 3:
        delete_student()
    elif choice == 4:
        print("Exiting program...")
        break
    else:
        print("Invalid choice! Try again.\n")