
# Student Practice Program

students = []

def add_student():
    name = input("Enter student name: ")
    roll = input("Enter roll number: ")
    marks = float(input("Enter marks: "))

    student = {
        "name": name,
        "roll": roll,
        "marks": marks
    }

    students.append(student)
    print("\nStudent added successfully!")

def show_students():
    if not students:
        print("\nNo students available.")
        return

    print("\n--- Student List ---")

    for s in students:
        print("Name:", s["name"])
        print("Roll No:", s["roll"])
        print("Marks:", s["marks"])
        print("--------------------")

while True:
    print("\n===== Student Practice =====")
    print("1. Add Student")
    print("2. Show Students")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        show_students()
    elif choice == "3":
        print("Program closed!")
        break
    else:
        print("Invalid choice!")
