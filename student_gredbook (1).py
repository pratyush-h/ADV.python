gradebook = {
    "Alice": 85,
    "Bob": 42,
    "Charlie": 78,
    "Diana": 92,
    "Eve": 55
}
def analyze_grades(data):
    print("Student Grade Report")
    total = 0    
    for student, grade in data.items():
        status = "Pass" if grade >= 60 else "Fail"
        print(f"{student}: {grade} ({status})")
        total += grade    
    average = total / len(data)
    print(f"Class Average: {average:.2f}")
analyze_grades(gradebook)