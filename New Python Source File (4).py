# 1. Initialize the student marks dictionary
student_marks = {
    "Alice": 85,
    "Bob": 78,
    "Charlie": 92
}

# 2. Add a new entry
student_marks["David"] = 88

# 3. Update an existing entry
# Alice retook a test and improved her score
student_marks["Alice"] = 95

# 4. Delete an entry
# Bob moved to a different school
del student_marks["Bob"]

# 5. Display keys, values, and items
print("--- Dictionary Metadata ---")
print(f"Keys (Student Names): {list(student_marks.keys())}")
print(f"Values (Grades):      {list(student_marks.values())}")

print("\n--- Full Items (Entries) ---")
for name, mark in student_marks.items():
    print(f"Student: {name} | Grade: {mark}")