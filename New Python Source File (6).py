students = {
    101: {"name": "Alice", "marks": [80, 90, 85]},
    102: {"name": "Bob", "marks": [70, 75, 80]}
}

def get_average(m): return sum(m) / len(m)

topper = max(students.items(), key=lambda x: get_average(x[1]["marks"]))
print(f"Topper: {topper[1]['name']} with Avg: {get_average(topper[1]['marks'])}")