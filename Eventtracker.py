
# Event Tracker System

entered_std = set()
rejected_std = set()

n = int(input("Enter Entry Attempts: "))

for i in range(n):
    name = input("Enter Student name: ")

    if name in entered_std:
        print(name, "Entry Rejected. Already Entered")
        rejected_std.add(name)
    else:
        print(name, "Entry Allowed")
        entered_std.add(name)

print("\n-- Event Tracker --")
print("Total Entered Students:", entered_std)
print("Rejected Students:", rejected_std)
rooms = {}

print("Room Allotment System")
n = int(input("Enter number of students: "))

for i in range(n):
    print("\nStudent", i+1)
    name = input("Enter student name: ")
    year = int(input("Enter year (1 to 4): "))

    if year == 1:
        room = "Room A1"
    elif year == 2:
        room = "Room B1"
    elif year == 3:
        room = "Room C1"
    elif year == 4:
        room = "Room D1"
    else:
        room = "Invalid year"

    rooms[name] = room

print("\n--- Final Room Allotment ---")
for student in rooms:
    print(student, "→", rooms[student])