# contact book
contacts = {}

def valid_phone(phone):
    return phone.isdigit() and len(phone) == 10

while True:
    print("\n1.Add Contact")
    print("2.Edit Contact")
    print("3.View Contacts")
    print("4.Save Contacts")
    print("5.Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone: ")

        if name == "" or phone == "":
            print("Error: Empty field")
        elif name in contacts:
            print("Error: Duplicate contact")
        elif not valid_phone(phone):
            print("Error: Phone must be 10 digits")
        else:
            contacts[name] = phone
            print("Contact added")

    elif choice == "2":
        name = input("Enter name to edit: ")

        if name not in contacts:
            print("Contact not found")
        else:
            phone = input("Enter new phone: ")
            if not valid_phone(phone):
                print("Invalid phone number")
            else:
                contacts[name] = phone
                print("Contact updated")

    elif choice == "3":
        for name, phone in contacts.items():
            print(name, "-", phone)

    elif choice == "4":
        file = open("contacts.txt", "w")
        for name, phone in contacts.items():
            file.write(name + "," + phone + "\n")
        file.close()
        print("Contacts saved")

    elif choice == "5":
        break

    else:
        print("Invalid choice")