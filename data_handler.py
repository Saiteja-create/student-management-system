import json
from school import Student  # import this for creating objects

def save_to_file(school, filename="students.json"):
    data = []
    for student in school.students:
        data.append({
            "name": student.name,
            "roll_number": student.roll_number,
            "marks": student.marks
        })
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)

def load_from_file(school, filename="students.json"):
    try:
        with open(filename, "r") as f:
            data = json.load(f)
            for entry in data:
                student = Student(entry["name"], entry["roll_number"])
                student.marks = entry["marks"]
                school.add_student(student)
    except FileNotFoundError:
        pass
