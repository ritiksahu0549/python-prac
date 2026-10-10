
# Student Management System

students = []

def add_student():
    name = input("Enter student name: ")
    roll_no = input("Enter roll number: ")
    marks = float(input("Enter marks (out of 100): "))

    student = {
        "name": name,
        "roll_no": roll_no,
        "marks": marks
    }

    students.append(student)
    print("Student added successfully!\n")


def display_students():
    if len(students) == 0:
        print("No student records found.\n")
        return

    print("\n----- Student Records -----")

    for student in students:
        print("Name:", student["name"])
        print("Roll Number:", student["roll_no"])
        print("Marks:", student["marks"])
        print("Result:", "Pass" if student["marks"] >= 33 else "Fail")
        print("---------------------------")


def search_student():
    roll_no = input("Enter roll number to search: ")

    for student in students:
        if student["roll_no"] == roll_no:
            print("\nStudent Found!")
            print("Name:", student["name"])
            print("Marks:", student["marks"])
            return

    print("Student not found.\n")


def calculate_average():
    if not students:
        print("No records available.\n")
        return

    total = sum(student["marks"] for student in students)
    average = total / len(students)

    print("Class Average:", round(average, 2), "\n")


while True:
    print("===== Student Management System =====")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Search Student")
    print("4. Calculate Class Average")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        display_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        calculate_average()
    elif choice == "5":
        print("Thank you for using the system!")
        break
    else:
        print("Invalid choice. Please try again.\n")
