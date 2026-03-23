records = []
records = []
for _ in range(int(input("Number of students: "))):
    name = input("Name: ")
    marks = int(input("Marks: "))
    records.append({"name": name, "status": "Pass" if marks >= 40 else "Fail"})

print([r for r in records if r["status"] == "Pass"])