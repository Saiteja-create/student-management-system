class Student:
    def __init__(self, name, roll_number):
        self.name = name
        self.roll_number = roll_number
        self.marks = {}

    def add_mark(self, subject, mark):
        self.marks[subject] = mark

    def get_average(self):
        if not self.marks:
            return 0
        total_marks = sum(self.marks.values())
        average = total_marks / len(self.marks)
        return average

    def get_grade(self):
        average = self.get_average()
        if average >= 90:
            return 'A'
        elif average >= 80:
            return 'B'
        elif average >= 70:
            return 'C'
        elif average >= 60:
            return 'D'
        else:
            return 'F'


class School:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def find_student(self, roll_number):
        for student in self.students:
            if student.roll_number == roll_number:
                return student
        return None  # if not found

    def display_all_students(self):
        for student in self.students:
            print(f"Name: {student.name} | Roll: {student.roll_number} | Avg: {student.get_average():.2f} | Grade: {student.get_grade()}")
