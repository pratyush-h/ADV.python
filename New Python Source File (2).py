student grade management
class StudentGradeSystem:
    def __init__(self):
        self.students = {}

    # Add student
    def add_student(self, student_id, grade):
        try:
            if student_id in self.students:
                print("Student ID already exists.")
                return

            if grade == "":
                raise ValueError("Grade cannot be empty.")

            grade = float(grade)
            self.students[student_id] = grade
            print("Student added successfully.")

        except ValueError:
            print("Invalid grade type. Please enter a numeric value.")

    # Update grade
    def update_grade(self, student_id, grade):
        try:
            if student_id not in self.students:
                raise KeyError("Invalid student ID.")

            if grade == "":
                raise ValueError("Grade cannot be empty.")

            grade = float(grade)
            self.students[student_id] = grade
            print("Grade updated successfully.")

        except KeyError:
            print("Student ID not found.")
        except ValueError:
            print("Invalid grade input.")

    # Delete student
    def delete_student(self, student_id):
        try:
            if student_id not in self.students:
                raise KeyError("Invalid student ID.")

            del self.students[student_id]
            print("Student deleted successfully.")

        except KeyError:
            print("Student ID not found.")

    # Display students
    def display_students(self):
        if not self.students:
            print("No student records available.")
        else:
            print("\nStudent Records:")
            for sid, grade in self.students.items():
                print(f"ID: {sid} | Grade: {grade}")


# Main Program
system = StudentGradeSystem()

while True:
    print("\n--- Student Grade Management System ---")
    print("1. Add Student")
    print("2. Update Grade")
    print("3. Delete Student")
    print("4. Display Students")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        sid = input("Enter Student ID: ")
        grade = input("Enter Grade: ")
        system.add_student(sid, grade)

    elif choice == "2":
        sid = input("Enter Student ID: ")
        grade = input("Enter New Grade: ")
        system.update_grade(sid, grade)

    elif choice == "3":
        sid = input("Enter Student ID: ")
        system.delete_student(sid)

    elif choice == "4":
        system.display_students()

    elif choice == "5":
        print("Exiting program...")
        break

    else:
        print("Invalid choice. Please try again.")