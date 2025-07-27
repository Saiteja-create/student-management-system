from school import Student, School

school = School()

def main_menu():
    while True:
        print("\n----- Student Management System -----")
        print("1. Add Student")
        print("2. Add Marks to Student")
        print("3. Show All Students")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            name = input("Enter student name: ")
            roll = input("Enter roll number: ")
            student = Student(name, roll)
            school.add_student(student)
            print("✅ Student added successfully.")

        elif choice == '2':
            roll = input("Enter roll number of the student: ")
            student = school.find_student(roll)
            if student:
                subject = input("Enter subject: ")
                mark = int(input("Enter mark: "))
                student.add_mark(subject, mark)
                print("✅ Mark added.")
            else:
                print("❌ Student not found.")

        elif choice == '3':
            school.display_all_students()

        elif choice == '4':
            print("👋 Exiting... Goodbye!")
            break

        else:
            print("❌ Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()

