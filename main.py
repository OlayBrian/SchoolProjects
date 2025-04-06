from student_service import StudentService

svc = StudentService()

while True:
    print("\nStudent Management System")
    print("1. Add Student")
    print("2. View Students")
    print("3. Delete Student")
    print("4. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        id = input("ID: ")
        name = input("Name: ")
        age = input("Age: ")
        grade = input("Grade: ")
        svc.add_student(id, name, age, grade)

    elif choice == "2":
        students = svc.get_students()
        for s in students:
            print(f"{s[0]} | {s[1]} | Age: {s[2]}, Grade: {s[3]}")

    elif choice == "3":
        svc.delete_student(input("Enter Student ID to delete: "))

    elif choice == "4":
        break

    else:
        print("Invalid choice, try again.")
